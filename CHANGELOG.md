# [1.14.0](https://github.com/de-it-krachten/ansible-role-facts/compare/v1.13.0...v1.14.0) (2025-03-21)


### Features

* Add fact for Windows hypervisor platform discovery ([8648e58](https://github.com/de-it-krachten/ansible-role-facts/commit/8648e58fd26f4e1a84c505797bf14082032473a8))

# [1.13.0](https://github.com/de-it-krachten/ansible-role-facts/compare/v1.12.0...v1.13.0) (2024-12-29)


### Features

* Update supported platforms & CI ([142bccc](https://github.com/de-it-krachten/ansible-role-facts/commit/142bccc618c1ab35b650d7e9dc9cf70742906c9b))

# [1.12.0](https://github.com/de-it-krachten/ansible-role-facts/compare/v1.11.0...v1.12.0) (2024-07-13)


### Bug Fixes

* Use loop_var names to avoid duplicates ([fb2bb89](https://github.com/de-it-krachten/ansible-role-facts/commit/fb2bb89ac637351bdf7b449d150d8db2565106f3))


### Features

* Remove support for RHEL/CentOS 7 ([d5c5d66](https://github.com/de-it-krachten/ansible-role-facts/commit/d5c5d66432e645577cfa1c17ea988b020d8a5b6c))

# [1.11.0](https://github.com/de-it-krachten/ansible-role-facts/compare/v1.10.2...v1.11.0) (2024-06-01)


### Features

* Add support for Ubuntu 24.04 LTS + Fedora 40 ([7ebc494](https://github.com/de-it-krachten/ansible-role-facts/commit/7ebc49423038a1833b9a48709e4f6641210bfde3))

## [1.10.2](https://github.com/de-it-krachten/ansible-role-facts/compare/v1.10.1...v1.10.2) (2024-04-12)


### Bug Fixes

* Add bool 'facts_force_run_setup' to forcingly execute setup ([c9efeaf](https://github.com/de-it-krachten/ansible-role-facts/commit/c9efeafad439d9134c462c6e14ccaa8411d13b95))

## [1.10.1](https://github.com/de-it-krachten/ansible-role-facts/compare/v1.10.0...v1.10.1) (2023-11-28)


### Bug Fixes

* Add variable to check for role execution in other roles ([04e1071](https://github.com/de-it-krachten/ansible-role-facts/commit/04e10712883926203cfa1437d01d9279a0b93a8a))

# [1.10.0](https://github.com/de-it-krachten/ansible-role-facts/compare/v1.9.0...v1.10.0) (2023-11-01)


### Features

* Add support for Windows ([6d4a9f8](https://github.com/de-it-krachten/ansible-role-facts/commit/6d4a9f8007a0f3e0faa8eef3b8059cb6c74ae7a7))

# [1.9.0](https://github.com/de-it-krachten/ansible-role-facts/compare/v1.8.0...v1.9.0) (2023-09-08)


### Features

* Add fact for mapper links ([ad7a73d](https://github.com/de-it-krachten/ansible-role-facts/commit/ad7a73ddbcd126a97518c2b0eb517e11c2a53143))
* Add facts for scsi devices ([a916829](https://github.com/de-it-krachten/ansible-role-facts/commit/a9168295dc5cf332a548887cefd17a446162b032))

# [1.8.0](https://github.com/de-it-krachten/ansible-role-facts/compare/v1.7.0...v1.8.0) (2023-08-14)


### Features

* Update supported platforms & CI ([0bcd4f6](https://github.com/de-it-krachten/ansible-role-facts/commit/0bcd4f6149bbc1bd2cc12ab9bc17720489fb1108))

# [1.7.0](https://github.com/de-it-krachten/ansible-role-facts/compare/v1.6.0...v1.7.0) (2023-05-06)


### Features

* Add support for slurm to assign a percentage of the total memory ([7751fc2](https://github.com/de-it-krachten/ansible-role-facts/commit/7751fc2603713302797b80e18cfdcd9c18beae5c))
* Add support kernel running & present ([400f3b6](https://github.com/de-it-krachten/ansible-role-facts/commit/400f3b61751eeb2053200fa4f5e69a6e98310f51))

# [1.6.0](https://github.com/de-it-krachten/ansible-role-facts/compare/v1.5.1...v1.6.0) (2023-01-12)


### Features

* Add cpu capabilities (virtualization support) ([ffdaa8e](https://github.com/de-it-krachten/ansible-role-facts/commit/ffdaa8ea8d78fa7b3bcc83fa365cca4a7df3fab8))
* Update CI/README/Platforms ([afe6db6](https://github.com/de-it-krachten/ansible-role-facts/commit/afe6db61878cc296d44ea8b4bfc31390b47682c7))

## [1.5.1](https://github.com/de-it-krachten/ansible-role-facts/compare/v1.5.0...v1.5.1) (2022-11-27)


### Bug Fixes

* Force user/group extended facts to run in bash ([0db8600](https://github.com/de-it-krachten/ansible-role-facts/commit/0db8600692ec2079ab7ce2a712f85c27ff4e6322))

# [1.5.0](https://github.com/de-it-krachten/ansible-role-facts/compare/v1.4.0...v1.5.0) (2022-11-27)


### Features

* Add Alpine to list of supported platforms ([51f3963](https://github.com/de-it-krachten/ansible-role-facts/commit/51f396366e94f1a45fe29ae2ac467849cdb2b39d))
* Add new custom facts 'users_ext' & 'groups_ext' ([d0e3103](https://github.com/de-it-krachten/ansible-role-facts/commit/d0e3103bd62657b444880e7592319a687768f093))

# [1.4.0](https://github.com/de-it-krachten/ansible-role-facts/compare/v1.3.0...v1.4.0) (2022-10-10)


### Features

* Move to FQCN ([3478fc9](https://github.com/de-it-krachten/ansible-role-facts/commit/3478fc932197c403714d2c401b224b914b1cf1fb))
* Update CI to latest standards ([0798920](https://github.com/de-it-krachten/ansible-role-facts/commit/07989202f1560c2b4a19088dd96e1130b93bc5d0))

# [1.3.0](https://github.com/de-it-krachten/ansible-role-facts/compare/v1.2.1...v1.3.0) (2022-07-28)


### Features

* Implement ansible-lint v6 support ([b81c153](https://github.com/de-it-krachten/ansible-role-facts/commit/b81c15386d6710bbab19127568c996e7af9bed64))

## [1.2.1](https://github.com/de-it-krachten/ansible-role-facts/compare/v1.2.0...v1.2.1) (2022-06-30)


### Bug Fixes

* fix some typo's in default varaibles ([51b45e8](https://github.com/de-it-krachten/ansible-role-facts/commit/51b45e8841fed1170c08652fdb2f86978bedd0fd))

# [1.2.0](https://github.com/de-it-krachten/ansible-role-facts/compare/v1.1.0...v1.2.0) (2022-06-30)


### Features

* add support for platform specifc facts ([48b1a41](https://github.com/de-it-krachten/ansible-role-facts/commit/48b1a4153d3cd81656cf03024ae41014a6af5348))

# [1.1.0](https://github.com/de-it-krachten/ansible-role-facts/compare/v1.0.0...v1.1.0) (2022-06-25)


### Bug Fixes

* Execute 'setup' directly and not via handlers ([ac1c789](https://github.com/de-it-krachten/ansible-role-facts/commit/ac1c7894567b1ef760e2d9ce456efa1efd3480c2))


### Features

* Add support for Ubuntu22.04+Fedora35/36 ([6413666](https://github.com/de-it-krachten/ansible-role-facts/commit/641366609613703f800f1dd185052307a5ddd595))

# 1.0.0 (2022-01-16)


### Features

* initial release ([e711de9](https://github.com/de-it-krachten/ansible-role-facts/commit/e711de92c5afb0a24233da515db15d7f7f6406fe))
