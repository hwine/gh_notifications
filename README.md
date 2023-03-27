# gh_notifications


`gh_notifications` is a library to access GitHub Notifications. It comes
with a cli & (eventually) a web interface.

Folks who work with many organizations which require SAML authentication
may find this tool more convenient to use, as authentication is handled
by a PAT (avoiding daily login to each SAML backed organization).

_N.B. this project is a learn-by-doing for me on library combined with
cli & web access using [`hatch`][hatch] & [`PyGithub`][pygithub]. Expect rough edges!_

**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

This is not packaged yet, so running from a clone is recommended.

```console
INSTALL_DIR=/path/to/parent/dir/gh_notifications
cd $INSTALL_DIR
cd ..
git clone https://github.com/hwine/gh_notifications.git
```

## Usage

The script uses [`hatch`][hatch], so that is the recommended approach for now. Install with:
```console
pipx install hatch
```

For the moment, it only lists unread notifications, grouped by
repository, via the command:
```console
cd $INSTALL_DIR
hatch run python -m gh_notifications
```


### Authentication

This script expects a (classic) PAT with permissions for `notifications` to be available as the value of the `GITHUB_TOKEN` environment variable. If you store that token in 1Password as "GH notification PAT", you can load it by sourcing the `load_gh_token` script.

## License

`gh-notifications` is distributed under the terms of the [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html) license.

[hatch]: https://hatch.pypa.io/latest/
[pygithub]: https://pygithub.readthedocs.io/
