[![CI](https://github.com/de-it-krachten/ansible-role-facts/workflows/CI/badge.svg?event=push)](https://github.com/de-it-krachten/ansible-role-facts/actions?query=workflow%3ACI)


# ansible-role-facts

Provisions several custom facts and runs setup optionally


Platforms
--------------

Supported platforms

- CentOS 7
- CentOS 8
- Debian 10 (Buster)
- Debian 11 (Bullseye)
- Ubuntu 18.04 LTS
- Ubuntu 20.04 LTS



Role Variables
--------------
<pre><code>
# default facts to distribute 
custom_facts:
  - users
  - groups

# customer facts to distribute
custom_facts_additional: []

# Run setup when facts change
custom_facts_setup: true
</pre></code>


Example Playbook
----------------

<pre><code>
- name: Converge
  hosts: all
  vars: null
  tasks:
    - name: Include role 'ansible-role-facts'
      include_role:
        name: ansible-role-facts
</pre></code>
