[![CI](https://github.com/de-it-krachten/ansible-role-facts/workflows/CI/badge.svg?event=push)](https://github.com/de-it-krachten/ansible-role-facts/actions?query=workflow%3ACI)


# ansible-role-facts

Provisions custom facts and runs setup optionally



## Dependencies

#### Roles
None

#### Collections
- ansible.windows

## Platforms

Supported platforms

- Red Hat Enterprise Linux 8<sup>1</sup>
- Red Hat Enterprise Linux 9<sup>1</sup>
- RockyLinux 8
- RockyLinux 9
- OracleLinux 8
- OracleLinux 9
- AlmaLinux 8
- AlmaLinux 9
- SUSE Linux Enterprise 15<sup>1</sup>
- openSUSE Leap 15
- Debian 11 (Bullseye)
- Debian 12 (Bookworm)
- Ubuntu 20.04 LTS
- Ubuntu 22.04 LTS
- Ubuntu 24.04 LTS
- Fedora 40
- Fedora 41
- Alpine 3
- Windows Server 2012 R2<sup>1</sup>
- Windows Server 2016<sup>1</sup>
- Windows Server 2019<sup>1</sup>
- Windows Server 2022<sup>1</sup>

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
  - name: kernel
  - name: users
  - name: users_ext
  - name: groups
  - name: groups_ext
  - name: repolist
    os_family: [ 'RedHat' ]
  - name: cpu
  - name: scsi
  - name: mapper

# customer facts to distribute
facts_custom_additional: "{{ custom_facts_additional | default([]) }}"

# Run setup when facts change
facts_run_setup: true

# Execute setup in all cases
facts_force_run_setup: false
</pre></code>

### defaults/family-Windows.yml
<pre><code>
# facts location
facts_path: c:\temp\facts

# list of defaults facts to distribute
# Possible attributes : name, groups (default=all), os (default=all), os_family (default=all)
# groups, os and os_family should be lists
facts_custom:
  - disks_custom

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
  become: 'yes'
  tasks:
    - name: Include role 'facts'
      ansible.builtin.include_role:
        name: facts
- name: sample playbook for role 'facts' post playbook
  ansible.builtin.import_playbook: converge-post.yml
  when: molecule_converge_post is undefined or molecule_converge_post | bool
</pre></code>
