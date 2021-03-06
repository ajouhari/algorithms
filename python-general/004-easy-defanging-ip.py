# Author: Abdulrahman Jouhari
# Date: June 21, 2020
# Project: Defanging an IP Address

# Instructions: Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')