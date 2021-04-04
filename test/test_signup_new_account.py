def test_signup_new_account(app):
    username = "sdasdasdsad"
    password = "tesasdasdasdt"
    app.james.ensure_user_exists(username, password)
