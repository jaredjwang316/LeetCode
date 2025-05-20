# -*- coding: utf-8 -*-
"""
Created on Tue May 20 16:26:06 2025

@author: jwang
"""

def numUniqueEmails(emails):
    """
    :type emails: List[str]
    :rtype: int
    """
    email_dict = dict()
    count_unique = 0
    for e in emails:
        parts = e.split('@')

        local_name = ""
        for ch in parts[0]:
            if ch == '.':   #mail sent there will be forwarded to the same address without dots in the local name. 
                continue
            elif ch == '+': #everything after the first plus sign gets ignored
                break
            else:
                local_name += ch
        
        domain_name = parts[1]

        if local_name not in email_dict:
            email_dict[local_name] = [domain_name]
            count_unique += 1
        else:
            if domain_name not in email_dict[local_name]:   #same local name can be for different types of email 
                count_unique += 1
            email_dict[local_name].append(domain_name)
    
    return count_unique

emails1 = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(numUniqueEmails(emails1))

emails2 = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
print(numUniqueEmails(emails2))