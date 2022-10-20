def update_user(backend, user, response, *args, **kwargs):
    user.role = "visitor"
    user.save()
