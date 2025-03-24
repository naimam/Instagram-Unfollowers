import streamlit as st
from PIL import Image
import json

def load_json(file):
    try:
        return json.load(file)
    except Exception as e:
        st.error(f"Error loading JSON: {e}")
        return None

def extract_users(data, key=None):
    users = []
    if key:
        data = data.get(key, [])

    for item in data:
        if 'string_list_data' in item and item['string_list_data']:
            users.append((item['string_list_data'][0]['value'], item['string_list_data'][0]['href']))
    return users

def main():
    st.set_page_config(page_title="Instagram Unfollowers Checker", page_icon="📷")

    st.title("Instagram Unfollowers Checker")

    st.write("Ever wondered who's unfollowed you on Instagram, but don't want to deal with sketchy apps asking for your "
    "account info or bombarding you with ads? This website is here to help! Just upload your data and get an instant,"
    " ad-free, and secure list of who’s not following you back—no strings attached.")

    st.write("Upload your Instagram `following.json` and `followers.json` files to see who isn't following you back.")

    with st.expander("How to download your Instagram following and followers data:"):
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
            <div style="display: flex; justify-content: space-between; padding: 10px 0;">
                <div><strong>👥 Following:</strong> {len(following)}</div>
                <div><strong>👤 Followers:</strong> {len(followers)}</div>
                <div><strong>🚫 Not Following Back:</strong> {len(not_following_back)}</div>
            </div>
            """, unsafe_allow_html=True)

            # Display Users Not Following Back
            if not_following_back:
                not_following_back = sorted(not_following_back, key=lambda x: x[0].lower())                 # sort alphabetically

                st.markdown("### 🚨 Users Not Following You Back:")

                for user, url in not_following_back:
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
if __name__ == "__main__":
    main()
