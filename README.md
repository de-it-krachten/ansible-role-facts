[![CI](https://github.com/de-it-krachten/ansible-role-facts/workflows/CI/badge.svg?event=push)](https://github.com/de-it-krachten/ansible-role-facts/actions?query=workflow%3ACI)


# ansible-role-facts

Provisions custom facts and runs setup optionally



## Dependencies

#### Roles
- deitkrachten.epel
- deitkrachten.python

#### Collections
- ansible.windows
- community.general

## Platforms

Supported platforms

- Red Hat Enterprise Linux 8<sup>1</sup>
- Red Hat Enterprise Linux 9<sup>1</sup>
- Red Hat Enterprise Linux 10<sup>1</sup>
- RockyLinux 8
- RockyLinux 9
- RockyLinux 10
- OracleLinux 8
- OracleLinux 9
- OracleLinux 10
- AlmaLinux 8
- AlmaLinux 9
- AlmaLinux 10
- Debian 11 (Bullseye)
- Debian 12 (Bookworm)
- Debian 13 (Trixie)
- Ubuntu 20.04 LTS
- Ubuntu 22.04 LTS
- Ubuntu 24.04 LTS
- Ubuntu 26.04 LTS
- Fedora 43
- Fedora 44<sup>1</sup>
- Alpine 3
- Windows Server 2012 R2<sup>1</sup>
- Windows Server 2016<sup>1</sup>
- Windows Server 2019<sup>1</sup>
- Windows Server 2022<sup>1</sup>
- Windows Server 2025<sup>1</sup>

Note:
<sup>1</sup> : no automated testing is performed on these platforms


## Role Variables
### defaults/main.yml
<pre><code>
# OS-oriented defaults
__facts_os_defaults:
  default:
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
      - name: platform
      - name: lsmod

    facts_packages:
      - kmod

    # List of tools to install in python venv
    facts_venv:
      - name: jc
        packages:
          - jc

    # Additional facts to distribute
    facts_custom_additional: "{{ custom_facts_additional | default([]) }}"

    # Run setup when facts change
    facts_run_setup: true

    # Execute setup in all cases
    facts_force_run_setup: false

  'family-Debian':
    # List of packages required to custom facts
    facts_packages:
      - kmod
      - python3-venv
  'family-Windows':
    # facts location
    facts_path: c:\temp\facts

    # list of defaults facts to distribute
    # Possible attributes : name, groups (default=all), os (default=all), os_family (default=all)
    # groups, os and os_family should be lists
    facts_custom:
      - disks_custom
      - platform
    # customer facts to distribute
    facts_custom_additional: "{{ custom_facts_additional | default([]) }}"
    # Run setup when facts change
    facts_run_setup: true
  'RedHat-10':
    facts_packages:
      - kmod
      - python3-packaging

# OS key helpers
__facts_distro: "{{ ansible_facts.distribution }}"
__facts_os_family: "{{ ansible_facts.os_family }}"
__facts_distro_version: "{{ __facts_distro }}-{{ ansible_facts.distribution_major_version }}"
__facts_os_version: "{{ __facts_os_family }}-{{ ansible_facts.distribution_major_version }}"

# Construct defaults in the corrct order
__facts_os: >-
  {{
    __facts_os_defaults['default'] | default({}) |
    combine(__facts_os_defaults['family-'+__facts_os_family] | default({})) |
    combine(__facts_os_defaults['family-'+__facts_os_version] | default({})) |
    combine(__facts_os_defaults[__facts_distro] | default({})) |
    combine(__facts_os_defaults[__facts_distro_version] | default({}))
  }}

# Public variables — all lazy, all overridable
facts_custom: "{{ __facts_os.facts_custom }}"
facts_custom_additional: "{{ __facts_os.facts_custom_additional }}"
facts_packages: "{{ __facts_os.facts_packages }}"
facts_path: "{{ __facts_os.facts_path }}"
facts_run_setup: "{{ __facts_os.facts_run_setup }}"
facts_force_run_setup: "{{ __facts_os.facts_force_run_setup }}"
facts_venv: "{{ __facts_os.facts_venv }}"
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
