# Jinja2 Workshop

This workshop is designed to test some templating skills.  Essentially, we are going to create a Jinja2-based report based on some variables and facts.  No variables should be hardcoded in the template.


The dynaimcally generated report should contain the following.  Each section in the report is to be identified by a category name (ie Users, States, etc), the formatting of the category element is up to you and should be followed by the data to be rendered.

**header**

1. A string notifying that this file is managed by ansible, as well as the timestamp when the report was generated.

**users**

1. A line separated list of users defined in `vars/vars.yml`, but not snoopy.  Each username should be preceeded by its loop index.

2. A CSV list of all the users defined in vars.yml.

**state**

1. The second state defined in `vars/vars.yml`, in lower-case.

**servers**

1. A list of all of the servers in the "myhosts" inventory group. **Note:** This is technically a different inventory that in the previous workshops


**setting**:

1. If `foo_setting` is defined, we want to declare it, otherwise, we want to make a comment noting that it is undefined.


**environment variables**

1. A line separated list of discovered environment variables and their values, sorted by key.
