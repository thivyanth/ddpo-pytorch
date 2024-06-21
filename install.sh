
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
sudo apt update
sudo apt upgrade
sudo apt install build-essential

RUSTUP_TOOLCHAIN=1.72.0 pip install tokenizers==0.13.2

# pip install torch==1.13.1+cu116 torchvision==0.14.1+cu116 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu116/torch_stable.html
pip install ml-collections
pip install absl-py
pip install diffusers[torch]==0.17.1
pip install accelerate==0.17
pip install wandb
pip install torchvision
pip install inflect==6.0.4
pip install pydantic==1.10.9
pip install transformers==4.30.2
