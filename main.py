from st_pages import Page, show_pages

"## Declaring the pages in your app:"

show_pages(
    [
        Page("pages/home.py", "Dasbor", "🏠"),
        # Page("pages/predict.py", "Predict Plate Number", "📝"),
        Page("pages/upload_predict.py", "Predict Plate Number", "📝")
    ]
)