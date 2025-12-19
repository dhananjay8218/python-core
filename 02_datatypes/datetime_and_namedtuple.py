# Chapter 11: Datetime & namedtuple
import arrow
from collections import namedtuple

# Current time
now = arrow.utcnow()
now_in_rome = now.to("Europe/Rome")
print("Time Rome:", now_in_rome)

# Namedtuple example
UserProfile = namedtuple("UserProfile", ["role", "level"])
profile = UserProfile(role="admin", level="high")

print("Profile:", profile)
print("Role:", profile.role)
