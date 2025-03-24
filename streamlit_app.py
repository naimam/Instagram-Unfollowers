import streamlit as st
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

    st.write("Upload your Instagram `following.json` and `followers.json` files to see who isn't following you back.")

    following_file = st.file_uploader("Upload following.json", type="json")
    followers_file = st.file_uploader("Upload followers.json", type="json")

    if following_file and followers_file:
        following_data = load_json(following_file)
        followers_data = load_json(followers_file)

        if following_data and followers_data:
            following = extract_users(following_data, 'relationships_following')
            followers = extract_users(followers_data)  

            not_following_back = set(following) - set(followers)

            st.write(f"### Following: {len(following)}")
            st.write(f"### Followers: {len(followers)}")
            st.write(f"### Users Not Following Back: {len(not_following_back)}")

            if not_following_back:
                st.write("### Users Not Following You Back:")
                for user, url in not_following_back:
                    st.markdown(f"- [{user}]({url})")
            else:
                st.success("Everyone you follow is following you back!")

if __name__ == "__main__":
    main()