#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 11:22:46 2021

@author: FelipeAffonso
"""

import streamlit as st
import numpy as np
import cv2
from PIL import Image, ImageEnhance

OUTPUT_WIDTH = 350

def main():
    st.title('Algumas operações em OpenCV')
    st.sidebar.title('Opções')
    
    #mudança de pagina
    opcoes_menu = ['Filtros', 'Sobre']
    st.sidebar.selectbox("Escolha uma Opção", opcoes_menu)
    
    #carregar e exibir a imagem
    image_file = st.file_uploader("Carregue uma foto e aplique um filtro no menu lateral", 
                                  type=['jpg', 'jpeg', 'png'])
    
    our_image = Image.open('empty.jpg')
    if image_file is not None:
        our_image = Image.open(image_file)
        st.sidebar.text("Imagem Original")
        st.sidebar.image(our_image, width=150)
        
        
    filtros = st.sidebar.radio("Filtros", ['Original', 'Grayscale', 'Desenho', 'Sépia', 'Blur'])
    
    if filtros == 'Grayscale':
        converted_image = np.array(our_image.convert('RGB'))
        gray_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2GRAY)
        st.image(gray_image, width=OUTPUT_WIDTH)
        
    elif filtros == 'Desenho':
        converted_image = np.array(our_image.convert('RGB'))
        gray_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2GRAY)
        inv_gray_image = 255 - gray_image
        blur_image = cv2.GaussianBlur(inv_gray_image, (21,21), 0,0)
        sketch_image = cv2.divide(gray_image, 255 - blur_image, scale=256)
        st.image(sketch_image, width=OUTPUT_WIDTH)
    
    elif filtros == 'Sépia':
        converted_image = np.array(our_image.convert('RGB'))
        converted_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2BGR)
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        sepia_image = cv2.filter2D(converted_image, -1, kernel)
        st.image(sepia_image, channels = "BGR", width=OUTPUT_WIDTH)
    
    elif filtros == 'Blur':
        b_amount = st.sidebar.slider('Tamanho do kernel (n x n)', 3, 81, 9, step=2)
        converted_image = np.array(our_image.convert('RGB'))
        converted_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2BGR)
        blur_image = cv2.GaussianBlur(converted_image, (b_amount,b_amount), 0,0)
        st.image(blur_image, channels = "BGR", width=OUTPUT_WIDTH)
    
    elif filtros == 'Canny':
        converted_image = np.array(our_image.convert('RGB'))
        converted_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2BGR)
        blur_image = cv2.GaussianBlur(inv_gray_image, (11,11), 0,0)
        canny = cv2.Canny(blur_image, 100, 150)
        st.image(canny, width=OUTPUT_WIDTH)
    
    elif filtros == 'Original':
        st.image(our_image, width=OUTPUT_WIDTH)
    else:
        st.image(our_image, width=OUTPUT_WIDTH)
    
        
if __name__ == '__main__':
    main()