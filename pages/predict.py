from ultralytics import YOLO
import glob
import pandas as pd
import time
from pages.combine import *
import streamlit as st
import pandas as pd
from streamlit_extras.colored_header import colored_header
from st_pages import add_page_title
import os


def main():
    # user_input = input("Masukkan lokasi folder berisi gambar yang ingin diprediksi (format .png): ")
    # filename_output = input('Masukkan nama output file : ')
    user_input = st.text_input('Masukkan lokasi folder berisi gambar yang ingin diprediksi (format .png): ')
    filename_output = "hasil"
    
    if user_input and filename_output:
        start_time = time.time()
        img_fns = glob.glob(user_input + '/*.png')

        model_path = 'assets/best.pt'
        model = YOLO(model_path)

        results = model.predict(img_fns)
        df_combined = combine_results(results, img_fns)

        df_combined = df_combined.sort_values(by='Name of File', key=lambda x: x.map(sorting_filename))
        df_combined = df_combined.reset_index().iloc[:, 1:3]

        df_combined.to_csv(f'{filename_output}.csv')

        end_time = time.time()
        colored_header(
            label="Lama Waktu Prediksi",
            description="",
            color_name="violet-70",
        )
        execution_time = end_time - start_time
        # print(f"Execution time: {execution_time:.2f} seconds")
        st.write(f"Execution time: {execution_time:.2f} seconds")
        
        colored_header(
            label="Hasil Prediksi",
            description="",
            color_name="violet-70",
        )
        st.dataframe(df_combined, use_container_width=True)

if __name__ == "__main__":
    add_page_title(layout="wide")
    colored_header(
        label="Masukkan lokasi Data",
        description="",
        color_name="violet-70",
    )
    main()
