# bert-network-packet-flow-header-payload

## Input

- Network Packet - HEX DATA
```
3ca6f60849b920b39957e74b0800450005c881dc0000f506c2790d235d2b86588b3301bbf95a94eccbfa554bbac980100085d54400000101080abcb794b10c6ab7722057d82613cc2c721b879ef00e6d925bca92a02d529fd587fd8e5a9cb93dd2a405d8315612500d7179cf7c01ca5e18cd137fe2044fe15898d5b42722f9e79bbc7431ce711171aa63a6b779367d745a0b5432fa326e8e7238d15033da601a4bb9c9bea464f6ca54b64698f31493d9da42fa6e0904a15fb1f944b96de8c55909f7e8780be2de10786b0ff623e503f94276a694bbf823686654ebcdafbfce9f5677e3d21ac1d25426a2be1badeadc5f29449a024419bba4d350ce7494563e9dabaa2c405e21a5fc918586193499139bd967d06ad188e8446ce0ddd406a336847bb64e1e70a73aaffdd1fdfc8cddd89b73433fe0fdcfe11dffa208710e0ecec840b632071872bb688353f59740f45d1efec153e2cc2b69f756b871073a8af9ca923eb213df7c1a67f5679d64e3e758394695fa486c32fd43d454bacc5b5f733eb5e28f70d605ff0947cf68e27dd51081b08ee083976d6b6eb277bd5e8787cb80e0bd574b6f6493e626999467e098ec329fd049d7d20ddc18547e2284e5560509692ce6e86fee5ece2997757697279dbbe418c37a86a79829b34cf8cb52e07e389c61373eff20705d8906aa6d98d5169bb316e963c6a85c8a4f5aea12d6e9a5402cb2aacc63be2b5a845bb5be1f416e19764f44b57837a854d233b764cbb8849f49a5c3deb77a0208cb512d973034c36d90870efdbad00c55fc3d85ef76fd275c21cf0cfbd6cf3cebbd0c62d3c4e8cb21a65b0983c1ed24d9f0a2bd1831316d62aeb6ec9e14a998803671b12d4dcf37151b75b69ec28cca72a36f67b5d3ec3f02606f94ebf941c0f705fd3ba39a154dcb20b1929df10c2ced9db7de3f2bfca59528e699591436b605ae5c174e3c3d7a237c72a0cce22d4cc370767d78a7ed485eb5fc96f6ae45e7e3114ecb1aab59acdcc14a7303b4f49484c2b834f8289e006bd4c6ae38018db9c48ea09caa095b25a0e626486713e07ca409ff52918d6bd390903db3b3a5f823cb91dab2d515c34f459c58dd242529322bc10428786451bd7c2d899f0398c9ffc37302b0d2dca95569d29db478705ed7c85a27ec00cb827c4671424ee33a49a80ec1e63b3a810af84ea42bdac72b6c9a5aa5438bdc4461a9bf3dafc676457072918c6c6a65aaed79a1be272f006edf7c2e930919a53a2eae0749d98cdd9c1b482d4db4adb7a9865ac613bb9a9d8110a72f3f4f40a58fe9fa8eec36e1eee61124d84e92001c617fb025e48e250a173e031552575b48e67d67c988c432364e945e5b3845d61090ccbb628504aac0d453a91c75fa23d6d59b65eadfe79c10f9878715780b9c5b68df37234ddd723b0023611c647f17fddaf0266eec2faa7e745fb06017cbcba1608fd3a9903036d3c5505a3185d0b31f512106509a4cc5582fe13283a18d817b95feb25a61782f2a571722c24979fb39efaf823be465483271e4c4dcc39a8cbc930492ed1b224aa37c50dc19e67b4f1117f92d0bd6ef81cbc72ac2189e27d893b838a19d7a2b8a9b46a6786fdbcfa3749cf564b0038440418a7c9fe2f477458ef743270aeafe0bf510f043a7e7d54787ab92ba80f97d75e06f4bc25cb521d54d221fd089d408d7c9166268376c5c2de1c2f44dc6c0402c35a0f55b2f3ea13f80a11a80f65d41bcb63dac7ae9cfa063a8c749231d6d2cd9b5a83252972f0dd424efa79b72bf558d1648dd2c78c202e7398eef6b8adeab334227e92534e7f3dd26bdaa856ce1feba77f87005e4ed87a6dae4c2bb2c72eecfaaf9e1299cb2f0ff1f3f8cff459e30396bf595d7c08a9a704a394211cc459e01a939cb6cbf8627ceefebb1b338d47079e3958009d2388b86e38a9a5c51f2134c304f98c21d00951c8aa15d3f47e9ba61fa43606d91698000bb7427365ef8b485d11bcdfcea0d52e40af2b76e9f3d372b15c9463b18660f23cd5f04e660f727467a34d8994b22f713f1bfaaf2cb1a0b2aaaa3b1caacd6955ec3e96fde2ca82b5caedc45521cb3978a7c3d65b4076ec96f069608
```

## Output

- Top classes for input_hex.txt
```
Normal : 100.000
DoS : 0.000
SSH Patator : 0.000
```

- Top classes for input_exploit.txt with tcp payload
```
Reconnaissance : 99.884
Exploits : 0.064
DoS : 0.027
```

- Top classes for input_exploit.txt with ip payload (--ip option)
```
Exploits : 95.659
DoS : 2.805
Reconnaissance : 1.065
```

## Requirements

This model requires additional module.

```
pip3 install transformers
pip3 install scapy
```

## Usage
Automatically downloads the onnx and prototxt files on the first run.
It is necessary to be connected to the Internet while downloading.

For the sample hex-data,
```bash
$ python3 bert-network-packet-flow-header-payload.py
```

If you want to specify the input hex file, put the file path after the `--input` option.  
```bash
$ python3 bert-network-packet-flow-header-payload.py --input HEX_FILE_PATH
```

If you want to specify the input hex data, put the hex value after the `--hex` option.  
```bash
$ python3 bert-network-packet-flow-header-payload.py --hex 3ca6f6...069608
```

If you want to use the IP packet for the Payload, specify the --ip option (TCP payload is used by default).
```bash
$ python3 bert-network-packet-flow-header-payload.py --ip
```

## Reference

- [Hugging Face - bert-network-packet-flow-header-payload](https://huggingface.co/rdpahalavan/bert-network-packet-flow-header-payload)
- [ESIR-S9 - AI Project : Network Traffic Analysis](https://github.com/TPs-ESIR-S9/PcapFileAnalysis/)

## Framework

Pytorch

## Model Format

ONNX opset=11

## Netron

[model.onnx.prototxt](https://netron.app/?url=https://storage.googleapis.com/ailia-models/bert-network-packet-flow-header-payload/model.onnx.prototxt)
