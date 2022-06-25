[![CI](https://github.com/de-it-krachten/ansible-role-facts/workflows/CI/badge.svg?event=push)](https://github.com/de-it-krachten/ansible-role-facts/actions?query=workflow%3ACI)


# ansible-role-facts

Provisions several custom facts and runs setup optionally

## Platforms

Supported platforms

- Red Hat Enterprise Linux 7<sup>1</sup>
- Red Hat Enterprise Linux 8<sup>1</sup>
- CentOS 7
- RockyLinux 8
- AlmaLinux 8<sup>1</sup>
- Debian 10 (Buster)
- Debian 11 (Bullseye)
- Ubuntu 18.04 LTS
- Ubuntu 20.04 LTS
- Ubuntu 22.04 LTS

Note:
<sup>1</sup> : no automated testing is performed on these platforms

## Role Variables
### defaults/main.yml
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



## Example Playbook
### molecule/default/converge.yml
<pre><code>
- name: sample playbook for role 'facts'
  hosts: all
  vars:
  tasks:
    - name: Include role 'facts'
      include_role:
        name: facts
</pre></code>
