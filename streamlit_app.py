import streamlit as st
import json
import pandas as pd

def load_json(file):
    try:
        # Check if file is empty
        if file.size == 0:
            st.error("Uploaded file is empty. Please upload a valid JSON file.")
            return None

        # Load JSON data
        data = json.load(file)

        return data
    except json.JSONDecodeError:
        st.error("Error decoding JSON. Please ensure the file contains valid JSON data.")
        return None
    except Exception as e:
        st.error(f"Unexpected error: {e}")
        return None

def extract_users(data, key=None):
    users = []
    if key:
        data = data.get(key, [])

    for item in data:
        if 'string_list_data' in item and item['string_list_data']:
            users.append((item['string_list_data'][0]['value'], item['string_list_data'][0]['href']))
    return users

def export_to_csv(users):
    df = pd.DataFrame(users, columns=['Username', 'Profile URL'])
    csv = df.to_csv(index=False)
    return csv


def main():
    st.set_page_config(page_title="Instagram Unfollowers Checker", page_icon="📷", initial_sidebar_state="expanded")

    st.title("Instagram Unfollowers Checker")

    st.write("Ever wondered who's unfollowed you on Instagram, but don't want to deal with sketchy apps asking for your "
    "account info or bombarding you with ads? This website is here to help!")

    st.write("Just upload your Instagram `following.json` and `followers.json` files and get an instant,"
    " ad-free, and secure list of who’s not following you back—no strings attached.")
    st.write("If you don't know how to download these files, check out the instructions in the sidebar.")

    # Sidebar with instructions
    with st.sidebar:
        st.header("How to download your Instagram following and followers data:")
        st.markdown("""
        1. **Access Instagram's Account Center:**
            - Open the Instagram app on your device.
            - Go to settings.
            - Open **"Accounts center."**
            - Under **"Account Settings,"** tap **"Your information and permissions."**
            - Alternatively, open this link [Instagram Account Center](https://accountscenter.instagram.com/info_and_permissions/dyi/).
        

        2. **Request Your Data:**
            - Scroll down and tap **"Download Your Information."**
            - Choose **"Download or transfer information."**
            - Select **"Some of your information"** and then under **"Connections,"** choose **"Followers and following"**. Then hit next.
            - Choose **"Download to device"**.
            - Choose your date range to be **"All time"** and the format to be **"JSON."**
            - Tap **"Create Files"** to initiate the request.

        3. **Download Your Data:**
            - Wait for Instagram to process your request (it may take some time).
            - You'll receive an email with a download link. Download the file within **four days**.
                    
        4. **Extract the Files:**
            - Extract the downloaded ZIP file.
            - You'll find two JSON files: `following.json` and `followers.json`.
            - Upload these files here to see who isn't following you back.

        For further assistance, visit [Instagram Help Center](https://help.instagram.com/181231772500920/?cms_platform=www&helpref=platform_switcher).
        """)

    following_file = st.file_uploader("Upload following.json", type="json")
    followers_file = st.file_uploader("Upload followers.json", type="json")


    if following_file and followers_file:
        following_data = load_json(following_file)
        followers_data = load_json(followers_file)

        if following_data and followers_data:
            following = extract_users(following_data, 'relationships_following')
            followers = extract_users(followers_data)

            not_following_back = set(following) - set(followers)

             # Display Stats
            st.markdown(f"""
            <div style="display: flex; justify-content: space-between; padding: 10px 0; font-size: 18px;">
                <div><strong>👥 Following:</strong> {len(following)}</div>
                <div><strong>👤 Followers:</strong> {len(followers)}</div>
                <div><strong>🚫 Not Following Back:</strong> {len(not_following_back)}</div>
            </div>
            """, unsafe_allow_html=True)

            # Display Users Not Following Back
            if not_following_back:
                not_following_back = sorted(not_following_back, key=lambda x: x[0].lower())                 # sort alphabetically



                # Export to CSV
                csv_data = export_to_csv(not_following_back) 
                st.markdown(
                    """
                    <div style="display: flex; justify-content: center; margin-top: 20px;">
                        <div>
                            <style>
                                .stDownloadButton button {
                                    margin: auto;
                                    display: block;
                                }
                                .stDownloadButton button:hover {
                                    color: blue;
                                    border-color: blue;
                            </style>
                            """,
                    unsafe_allow_html=True,
                )
                st.download_button("Download CSV File of IG Unfollowers", csv_data, "instagram_unfollowers.csv", "text/csv")



                st.markdown("### 🚨 Users Not Following You Back:")

                for user, url in not_following_back:
                    #User List Display
                    st.markdown(f"""
                    <a href="{url}" target="_blank" style="text-decoration: none; color: inherit;">
                        <div style="
                            display: flex; 
                            align-items: center; 
                            margin-bottom: 15px; 
                            padding: 10px; 
                            border-radius: 12px; 
                            background-color: #f9f9f9; 
                            box-shadow: 2px 2px 8px rgba(0,0,0,0.1); 
                            transition: transform 0.2s ease;
                        " onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
                            <img src="https://i.imgur.com/PezIUJX.png" style="height: 20px; border-radius: 50%; margin-right: 15px;">
                            <span style="font-weight: bold; font-size: 16px;">{user}</span>
                        </div>
                    </a>
                    """, unsafe_allow_html=True)
            else:
                st.success("🎉 Everyone you follow is following you back!")

    # Ko-fi link integration
    st.markdown(""" 
      <p style="display: flex; justify-content: center; margin: 20px;"> Consider supporting me by buying me a coffee ☕️ if you find this tool helpful: </p>

        <div style="display: flex; justify-content: center; margin: 20px;">
            <a href='https://ko-fi.com/R5R71CFRC2' target='_blank'>
                <img height='36' style='border:0px;height:36px;' 
                    src='https://storage.ko-fi.com/cdn/kofi5.png?v=6' 
                    border='0' 
                    alt='Buy Me a Coffee at ko-fi.com' />
            </a>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
