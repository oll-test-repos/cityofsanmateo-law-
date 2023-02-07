# SMC test auth repo

## Generate instructions

1. Create (and modify if needed) *keys.json* file:

    ```json
    {
        "root": {
            "number": 2,
            "threshold": 1
        },
        "targets": {
            "number": 1,
            "threshold": 1,
            "delegations": {
                "law": {
                    "paths": [
                        "cityofsanmateo/law-xml",
                        "cityofsanmateo/law-html",
                        "cityofsanmateo/law-xml-codified",
                        "capstone",
                        "branch"
                    ],
                    "number": 1,
                    "threshold": 1,
                    "terminating": true
                },
                "docs":{
                    "paths": [
                        "cityofsanmateo/law-docs"
                    ],
                    "number": 1,
                    "threshold": 1,
                    "terminating": true
                },
                "assets":{
                    "paths": [
                        "cityofsanmateo/law-static-assets"
                    ],
                    "number": 1,
                    "threshold": 1,
                    "terminating": true
                }
            }
        },
        "snapshot": {},
        "timestamp": {}
    }
    ```

1. Create initial metadata: `taf repo create .\smc-law-test --keys-description keys.json --keystore .\keystore\  --test`

1. Create *.gitattributes* file:

    ```txt
    # These settings are for any web project

    # Handle line endings automatically for files detected as text
    # and leave all files detected as binary untouched.
    * text=auto

    # Force the following filetypes to have unix eols, so Windows does not break them
    *.* text eol=lf

    #
    ## These files are binary and should be left untouched
    #

    # (binary is a macro for -text -diff)
    *.png binary
    *.jpg binary
    *.jpeg binary
    *.gif binary
    *.ico binary
    *.mov binary
    *.mp4 binary
    *.mp3 binary
    *.flv binary
    *.fla binary
    *.swf binary
    *.gz binary
    *.zip binary
    *.7z binary
    *.ttf binary
    *.eot binary
    *.woff binary
    *.pyc binary
    *.pdf binary
    *.ez binary
    *.bz2 binary
    *.swp binary
    *.whl binary
    ```

1. Create *requirements.txt* file:

    ```txt
    oll-partners # oll.partners.us.ca.cities.san_mateo
    ```

1. **Commit changes**

1. Create `repositories.json`, add it to `./targets` directory and modify if needed:

    ```json
    {
        "repositories": {
            "cityofsanmateo/law-docs": {
                "urls": [
                    "https://github.com/openlawlibrary/law-docs.git"
                ],
                "custom": {
                    "type":"docs",
                    "allow-unauthenticated-commits":true
                }
            },
            "cityofsanmateo/law-html": {
                "urls":[
                    "https://github.com/openlawlibrary/law-html.git"
                ],
                "custom": {
                    "preview":"https://github.com/openlawlibrary/law-html-preview.git",
                    "type":"html"
                }
            },
            "cityofsanmateo/law-xml": {
                "urls": [
                    "https://github.com/openlawlibrary/law-xml"
                ],
                "custom": {
                    "type":"xml",
                    "allow-unauthenticated-commits":true
                }
            },
            "cityofsanmateo/law-xml-codified": {
                "urls": [
                    "https://github.com/openlawlibrary/law-xml-codified.git"
                ],
                "custom": {
                    "preview":"https://github.com/openlawlibrary/law-xml-codified-preview.git",
                    "type":"xml-codified"
                }
            },
            "cityofsanmateo/law-static-assets": {
                "urls": [
                    "https://github.com/openlawlibrary/law-static-assets.git"
                ],
                "custom": {
                    "type":"law-static-assets",
                    "allow-unauthenticated-commits":true
                }
            }
        }
    }
    ```

1. sign *repositories.json*: `taf targets sign .\smc-law-test\ --keystore .\keystore\`

1. Copy *appveyor.yml* from: https://gist.github.com/danixeee/62b72008ac2a1e07614a500a8b897d82

1. Commit & push
