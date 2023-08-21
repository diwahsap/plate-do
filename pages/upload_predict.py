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
import zipfile


def main():
    user_input = st.file_uploader("Upload your file!", type=["zip"])
    # extract zip file to folder temp/temp
    if user_input is not None:
        # clear all file in temp/temp
        files = glob.glob('temp/temp/*')
        for f in files:
            os.remove(f)    

        # extract zip file to folder temp/temp
        if user_input.type == "application/zip":
            # if folder temp/temp not empty, clear all file in temp/temp
            with zipfile.ZipFile(user_input, "r") as z:
                z.extractall(path='temp/temp')

        start_time = time.time()
        img_fns = glob.glob("temp/temp" + '/*.png')

        model_path = 'assets/best.pt'
        model = YOLO(model_path)

        results = model.predict(img_fns)
        df_combined = combine_results(results, img_fns)

        df_combined = df_combined.sort_values(by='Name of File', key=lambda x: x.map(sorting_filename))
        df_combined = df_combined.reset_index().iloc[:, 1:3]

        df_combined.to_csv(f'hasil.csv')

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
        label="Upload Dataset",
        description="",
        color_name="violet-70",
    )
    main()
