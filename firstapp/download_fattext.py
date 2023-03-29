import os
import wget
import gzip
import shutil

def download_fasttext_model():
    model_url = "https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.fr.300.bin.gz"
    model_gz = "cc.fr.300.bin.gz"
    model_path = "fasttext_french.bin"

    if not os.path.exists(model_path):
        print("Downloading FastText model...")
        wget.download(model_url, model_gz)
        print("Extracting FastText model...")
        with gzip.open(model_gz, 'rb') as f_in:
            with open(model_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        os.remove(model_gz)
        print("FastText model downloaded and extracted successfully!")

if __name__ == "__main__":
    download_fasttext_model()
