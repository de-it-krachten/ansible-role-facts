[![CI](https://github.com/de-it-krachten/ansible-role-facts/workflows/CI/badge.svg?event=push)](https://github.com/de-it-krachten/ansible-role-facts/actions?query=workflow%3ACI)


# ansible-role-facts

Provisions several custom facts and runs setup optionally



## Dependencies

#### Roles
None

#### Collections
- community.general

## Platforms

Supported platforms

- Red Hat Enterprise Linux 7<sup>1</sup>
- Red Hat Enterprise Linux 8<sup>1</sup>
- Red Hat Enterprise Linux 9<sup>1</sup>
- CentOS 7
- RockyLinux 8
- RockyLinux 9
- OracleLinux 8
- AlmaLinux 8
- AlmaLinux 9
- Debian 10 (Buster)
- Debian 11 (Bullseye)
- Ubuntu 18.04 LTS
- Ubuntu 20.04 LTS
- Ubuntu 22.04 LTS
- Fedora 35
- Fedora 36

Note:
<sup>1</sup> : no automated testing is performed on these platforms

## Role Variables
### defaults/main.yml
<pre><code>
# facts location
facts_path: /etc/ansible/facts.d

# list of defaults facts to distribute 
# Possible attributes : name, groups (default=all), os (default=all), os_family (default=all)
# groups, os and os_family should be lists
facts_custom:
  - name: users
  - name: groups
  - name: repolist
    os_family: [ 'RedHat' ]

# customer facts to distribute
facts_custom_additional: "{{ custom_facts_additional | default([]) }}"

# Run setup when facts change
facts_run_setup: true
</pre></code>




## Example Playbook
### molecule/default/converge.yml
<pre><code>
- name: sample playbook for role 'facts'
  hosts: all
  become: "{{ molecule['converge']['become'] | default('yes') }}"
  vars:
    custom_facts_additional: [{'name': 'fact1', 'groups': 'all'}, {'name': 'fact2', 'os_family': ['RedHat']}, {'name': 'fact3', 'group': 'group1'}, {'name': 'fact4', 'groups': ['group2']}]
  tasks:
    - name: Include role 'facts'
      ansible.builtin.include_role:
        name: facts
</pre></code>
