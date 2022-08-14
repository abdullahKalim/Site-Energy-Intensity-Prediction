#!/usr/bin/env python
# coding: utf-8

# In[1]:


def encode_facility_type(facility_type):
    if(facility_type=="Laboratory"):
        return 3
    elif (facility_type=="Data_Center"):
        return 4
    elif("Health" in facility_type):
        return 2
    else:
        return 1


# In[2]:


def encode_building_class(building_class):
    if(building_class=="Commercial"):
        return 0
    else:
        return 1


# In[3]:


def predict(model,data):
    return model.predict(data)


# In[ ]:




