# remote_template workshop

Renders a template based on a remote source.  Feel free to change the remote source in the playbook to some other valid Jinja!


	ansible-playbook -i hosts -v test.yml
	
Should render

	cat /tmp/remote_template
	This is is not exciting..