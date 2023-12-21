import sys
import time

from einops import rearrange
import ailia
import cv2
import numpy as np

sys.path.append('../../util')
from logging import getLogger  # noqa: E402

import webcamera_utils  # noqa: E402
from image_utils import imread  # noqa: E402
from model_utils import check_and_download_models  # noqa: E402
from utils import get_base_parser, update_parser  # noqa: E402

logger = getLogger(__name__)

WEIGHT_PATH = "drbn_skf_lol.onnx"
MODEL_PATH = "drbn_skf_lol.onnx.prototxt"
REMOTE_PATH = 'https://storage.googleapis.com/ailia-models/drbn_skf/'
IMAGE_PATH = 'input.png'
SAVE_IMAGE_PATH = 'output.png'
HEIGHT_SIZE = 400
WIDTH_SIZE = 600

parser = get_base_parser(
    "DRBN_SKF",
    IMAGE_PATH,
    SAVE_IMAGE_PATH,
)
parser.add_argument(
    "-ver", 
    "--version",
    default=1,
    type=int,
    help="DRBN SKF version (select 1 or 2)",
)
args = update_parser(parser)

def get_model(model_path, weight_path, env_id, mem_mode):
    return ailia.Net(model_path, weight_path, env_id=env_id, memory_mode=mem_mode)


def recognize_from_image(weight_path, model_path):
    env_id = args.env_id
    mem_mode = ailia.get_memory_mode(reduce_constant=True, reduce_interstage=True)
    net = get_model(model_path, weight_path, env_id, mem_mode)

    for image_path in args.input:
        logger.info(image_path)
        img = imread(image_path) / 255.
        H, W = img.shape[:2]
        img = cv2.resize(img, (WIDTH_SIZE, HEIGHT_SIZE), interpolation=cv2.INTER_LANCZOS4)
        img = img[np.newaxis, :]
        img = rearrange(img, "1 h w c -> 1 c h w")
        logger.info(f"input image shape: {img.shape}")
        logger.info("Start inference ...")
        if args.benchmark:
            logger.info("BENCHMARK mode")
            for i in range(5):
                start = int(round(time.time() * 1000))
                pred = net.run(img)[0]
                end = int(round(time.time() * 1000))
                logger.info(f"\tailia processing time {end - start} ms")
        else:
            pred = net.run(img)[0]
    
            pred = rearrange(pred, "1 c h w -> h w c")
        enhance = cv2.resize(pred, (W, H), interpolation=cv2.INTER_LANCZOS4)
        enhance = np.clip(enhance, 0.0, 1.0)
        output = (enhance * 255.).astype(np.uint8)
        
        # save result
        logger.info(f"saved at : {args.savepath}")
        cv2.imwrite(args.savepath, output)

    logger.info("Script finished successfully.")


def recognize_from_video(weight_path, model_path):
    env_id = args.env_id
    mem_mode = ailia.get_memory_mode(reduce_constant=True, reduce_interstage=True)
    net = get_model(model_path, weight_path, env_id, mem_mode)
    capture = webcamera_utils.get_capture(args.video)

    f_h = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    f_w = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    
    if args.savepath != SAVE_IMAGE_PATH:
        logger.warning(
            "currently, video results cannot be output correctry..."
        )
        writer = webcamera_utils.get_writer(args.savepath, f_h, f_w, rgb=True)
    else:
        writer = None
    
    frame_shown = False
    while True:
        ret, frame = capture.read()
        if (cv2.waitKey(1) & 0xff == ord("q")) or not ret:
            break
        if frame_shown and cv2.getWindowProperty("frame", cv2.WND_PROP_VISIBLE) == 0:
            break

        img = cv2.resize(frame, (WIDTH_SIZE, HEIGHT_SIZE), interpolation=cv2.INTER_LANCZOS4) / 255.
        img = img[np.newaxis, :]
        img = rearrange(img, "1 h w c -> 1 c h w")
        pred = net.run(img)[0]
        pred = rearrange(pred, "1 c h w -> h w c")
        enhance = cv2.resize(pred, (f_w, f_h), interpolation=cv2.INTER_LANCZOS4)
        enhance = np.clip(enhance, 0.0, 1.0)
        output = (enhance * 255.).astype(np.uint8)
        concat = np.hstack((frame, output))
        cv2.imshow("left: original, right: result", concat)

        if writer is not None:
            writer.write(output)
    
    if not writer is None:
        writer.release()


def main():
    version = args.version
    weight_path= WEIGHT_PATH.replace("lol", f"lol_v{version}")
    model_path= MODEL_PATH.replace("lol", f"lol_v{version}")
    # check_and_download_models(weight_path, model_path, REMOTE_PATH)

    if args.video is None:
        recognize_from_image(weight_path, model_path)
    else:
        recognize_from_video(weight_path, model_path)


if __name__ == '__main__':
    main()
