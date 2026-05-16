from huggingface_hub import login

print("=====================================================================================================")
print("Please paste your Hugging Face Access Token below and press ENTER.")
print("Get your token from: https://huggingface.co/settings/tokens")
print("Make sure the token has 'Read' permissions.")
print("=====================================================================================================")

try:
    token = input("Token: ").strip()
    if not token:
        print("Error: No token provided.")
    else:
        login(token=token, add_to_git_credential=True)
        print("\nSUCCESS: You are logged in!")
except Exception as e:
    print(f"\nERROR: Login failed. Details: {e}")
