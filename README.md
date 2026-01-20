# dropout_tools

A collection of random scripts

## Included utilities

### `dropout_chroot`

Despite the name, this is not a direct equivalent to `chroot(1)`. It's also not a sandbox.

Intended for running small separate environments as unprivileged user.

Linux-specific.

#### Documentation

You need to prepare a rootfs directory containing a system. Many Linux distros provide tarballs which you'd grab and extract.

Running this command with the path, would enter the system.

Most distros use GNU Bash as default shell, so you might want to pass `-s /bin/bash` to this command.

This command by default uses root user inside the new system, but you can create another, by doing something like this after you've entered your system:

```shell
useradd -m -u 1000 dropout
```

As an example, to use this new user we've just created, add `-u 1000 -g 1000 -d /home/dropout` to your command when entering the system.

Note that no matter which user you use, all files inside your system are always writable, including system ones.

##### Installing Alpine Linux

Alpine provided "Mini root filesystem" on their [download page](https://www.alpinelinux.org/downloads/).

##### Installing Ubuntu

[Ubuntu Base](https://wiki.ubuntu.com/Base#To_download_Ubuntu_Base) can be used.

To be able to use `apt`, you'll need to write these lines in your `/etc/apt/apt.conf`:

```plaintext
APT::Sandbox::User "";
```

##### Installing Arch Linux

You'd download "bootstrap tarball" from [download page](https://archlinux.org/download/).

When you extract, you might also want to pass these arguments to `tar`:

```shell
--delay-directory-restore --strip-components=1 --wildcards root.x86_64/\*
```

To be able to use `pacman`, you'll need to uncomment these lines in your `/etc/pacman.conf`:

```ini
#DisableSandboxFilesystem
#DisableSandboxSyscalls
```

You'd also need to run these two commands as mentioned in [Arch Wiki](https://wiki.archlinux.org/title/Install_Arch_Linux_from_existing_Linux#Initializing_pacman_keyring).
