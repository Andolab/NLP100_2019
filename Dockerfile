From circleci/python:3.7

RUN sudo pip install -U pip \
    && sudo apt install -y swig mecab libmecab-dev mecab-ipadic-utf8 \
    && sudo curl -L -o CRF++-0.58.tar.gz 'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7QVR6VXJ5dWExSTQ' \
    && sudo tar zxf CRF++-0.58.tar.gz \
    && cd CRF++-0.58/ \
    && sudo ./configure \
    && sudo make \
    && sudo make install \
    && sudo ldconfig \
    && cd ../ \
    && sudo curl -c cabocha-0.69.tar.bz2 -s -L 'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7SDd1Q1dUQkZQaUU' | grep confirm |  sed -e "s/^.*confirm=\(.*\)&amp;id=.*$/\1/" | xargs -I{} \
        sudo curl -b cabocha-0.69.tar.bz2 -L -o cabocha-0.69.tar.bz2 'https://drive.google.com/uc?confirm={}&export=download&id=0B4y35FiV1wh7SDd1Q1dUQkZQaUU' \
    && sudo tar xjf cabocha-0.69.tar.bz2 \
    && cd cabocha-0.69 \
    && sudo ./configure --with-mecab-config='which mecab-config' --with-charset=UTF8 \
    && sudo make \
    && sudo make install \
    && sudo ldconfig \
    && cd python \
    && sudo python setup.py install \
    && cd ../../ \
    && sudo rm -rf CRF++-0.58* cabocha-0.69* \
    && sudo git clone https://github.com/brendano/stanford_corenlp_pywrapper \
    && cd stanford_corenlp_pywrapper \
    && sudo pip install . \
    && cd ../ \
    && sudo rm -rf stanford_corenlp_pywrapper
