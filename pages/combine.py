import pandas as pd
import os


def sorting_filename(filename):
    return int(''.join(filter(str.isdigit, filename)))


def combine_results(results, img_fns):
    combined_data = []

    for result, img_fn in zip(results, img_fns):
        boxes = result.boxes.cpu().numpy()
        sorted_detections = []

        for box in boxes:
            r = box.xyxy[0].astype(int)
            class_label = result.names[int(box.cls[0])]
            sorted_detections.append({'box': r, 'class_label': class_label})

        sorted_detections.sort(key=lambda x: x['box'][0])

        concatenated_labels = ""
        for detection in sorted_detections:
            concatenated_labels += detection['class_label']

        combined_data.append({'Name of File': img_fn, 'Vehicleregistrationplatebymodel': concatenated_labels})

    df_combined = pd.DataFrame(combined_data)
    df_combined['Name of File'] = df_combined['Name of File'].apply(lambda path: os.path.basename(path))

    return df_combined