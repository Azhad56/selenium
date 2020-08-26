from instapy import InstaPy
session = InstaPy(username="azhad.ghufran", password="Dabkdi@126814",headless_browser=False)
session.login()

#settings
session.set_do_follow(True, percentage=100)
session.set_do_like(enabled=True, percentage=100)
session.set_user_interact(amount=3, randomize=True, percentage=100, media="Photo")

#activity
session.like_by_tags(["photooftheday","instagood","nofilter","tbt","igers","picoftheday","love","swag","lifeisgood","selfie","bestoftheday","followme","Banglore","Panjab","Travel","Foodlover","sexy","Girls","Nightout","Nature","Instagram","Photography"], amount=1, interact=True, media="Photo")

session.end()
