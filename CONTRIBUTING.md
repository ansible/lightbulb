# Contribute

We take pull requests!  Please read the [PHILOSOPHY.md](PHILOSOPHY.md) and search the issues before submitting a PR.

## Create a Fork

Create a fork on your own GitHub project (or your personal space)

[GitHub Documentation on Forking a repo](https://help.github.com/articles/fork-a-repo/)

## Stay in Sync

It is important to know how to keep your fork in sync with the upstream Lightbulb project.

### Configuring Your Remotes

Configure Lightbulb as your upstream so you can stay in sync

```bash
git remote add upstream https://github.com/ansible/lightbulb.git
```

### Rebasing Your Branch

Three step process

```bash
git pull --rebase upstream master
```

```bash
git status
```

### Updating your Pull Request

```bash
git push --force
```

More info on docs.ansible.com: [Rebasing a Pull Request](http://docs.ansible.com/ansible/latest/dev_guide/developing_rebasing.html)

## Coding Guidelines

Style guides are important because they ensure consistency in the content, look, and feel of a book or a website.

* [Ansible Style Guide](http://docs.ansible.com/ansible/latest/dev_guide/style_guide/)
* Use Standard American English. Red Hat has customer all around the globe, but is headquarters in the USA
* It's "Ansible" when referring to the product and ``ansible`` when referring to the command  line tool, package, etc
* Playbooks should be written in multi-line YAML with ``key: value``. The form ``key=value`` is only for ``ansible`` ad-hoc, not for ``ansible-playbook``.
* Tasks should always have a ``name:``

### Markdown

To ensure consistency we use [Markdown lint](https://github.com/markdownlint/markdownlint). This is run against every pull request to the ``ansible/lightbulb`` repo. Our markdown standard is defined in [.mdlrc](.mdlrc)

If you wish to run this locally you can do so with:

```bash
gem install mdl
mdl -c .mdlrc .
```

## Create a pull requests

Make sure you are not behind (in sync) and then submit a PR to Lightbulb. [Read the Pull Request Documentation on github.com](https://help.github.com/articles/creating-a-pull-request/)

Just because you submit a PR, doesn't mean that it will get accepted.  Right now the QA process is manual for lightbulb, so provide detailed directions on

* WHY? Why did you make the change?
* WHO? Who is this for?  If this is something for a limited audience it might not make sense for all lightbulb users.  Refer to the [Lighbulb Philosophy](PHILOSOPHY.md)
* BEST PRACTICE?  Is this the "best" way to do this?  Link to documentation or examples where the way you solved your issue or improved Lightbulb is the best practice for teaching or building workshops.

Being more descriptive is better, and has a higher change of getting merged upstream.  Communication is key!  Just b/c the PR doesn't get accepted right away doesn't mean it is not a good idea.  Lightbulb has to balance many different types of users.  Thank you for contributing!

## Going Further

The following links will be helpful if you want to contribute code to the Lightbulb project, or any Ansible project:

* [Ansible Committer Guidelines](http://docs.ansible.com/ansible/latest/committer_guidelines.html)
* [Learning Git](https://git-scm.com/book/en/v2)
