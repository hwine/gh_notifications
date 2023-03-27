# gh_notifications


-----

`gh_notifications` is a library to access GitHub Notifications. It comes
with a cli & web interface.

Folks who work with many organizations which require SAML authentication
may find this tool more convenient to use, as authentication is handled
by a PAT (avoiding daily login to each SAML backed organization).

_N.B. this project is a learn-by-doing for me on library combined with
cli & web access using `hatch` & `PyGithub`. Expect rough edges!_

**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

```console
pip install .
```

## Usage

For the moment, it only lists unread notifications, grouped by
repository, via the command:
```console
python -m gh_notifications
```

## License

`gh-notifications` is distributed under the terms of the [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html) license.
