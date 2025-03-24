# Instagram Unfollowers Checker

A Streamlit web app that allows you to check who isn’t following you back on Instagram by uploading your `following.json` and `followers.json` files. The app is ad-free, secure, and simple to use. You can also download the list of users who aren't following you back in CSV format.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://instagramunfollowers.streamlit.app/)

## 🛠️ Tools Used

- **Streamlit**: For building the interactive web app and hosting it on streamlit cloud.
- **Pandas**: To handle CSV export functionality.
- **JSON**: To handle the uploaded JSON files.

## 🚀 How to Run Locally

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```


## 📄 Features

- **Upload JSON files**: Upload your `following.json` and `followers.json` files from Instagram.
- **View Stats**: The app shows how many users you're following, how many follow you back, and who isn’t following you back.
- **Export CSV**: Download the list of users who aren’t following you back in CSV format.


## 👥 Credits
**Flaticon**: The profile icon used in the app was sourced from [Flaticon](https://www.flaticon.com) with credits to the creator [QudaDesign](https://www.flaticon.com/authors/qudadesign).


## 📜 License
This project is open-source and available under the [MIT License](LICENSE).