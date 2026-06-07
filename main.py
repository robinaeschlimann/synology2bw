import pandas as pd

if __name__ == '__main__':
    df_source = pd.read_csv("c2export.csv")

    df_dest = pd.DataFrame()

    df_dest["folder"] = df_source["Tag"]
    df_dest["favorite"] = df_source["Favorite"]
    df_dest["type"] = "login"
    df_dest["name"] = df_source["Display_Name"]
    df_dest["notes"] = df_source["Notes"]
    df_dest["fields"] = ""
    df_dest["reprompt"] = "0"
    df_dest["login_uri"] = df_source["Login_URLs"]
    df_dest["login_username"] = df_source["Login_Username"]
    df_dest["login_password"] = df_source["Login_Password"]
    df_dest["login_totp"] = df_source["Login_TOTP"]

    # Ensure column order
    df_dest = df_dest[
        [
            "folder",
            "favorite",
            "type",
            "name",
            "notes",
            "fields",
            "reprompt",
            "login_uri",
            "login_username",
            "login_password",
            "login_totp",
        ]
    ]

    df_dest.to_csv("output.csv", index=0)
