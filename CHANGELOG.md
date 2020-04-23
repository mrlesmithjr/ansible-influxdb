commit 8b1b87bf07094ae3c07ecf6ea9147015a5adf8fc
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Apr 23 01:53:55 2020 -0400

    Changed version to 1.8.0 as 1.7.1 is not available
    
    Found this while testing fix for issue #12

commit eac6be27849938c6c8f48b7afdc30c5d61b52f8a
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Feb 21 18:25:37 2020 -0500

    Added Debian pre-reqs
    
    - Missing apt-transport-https

commit b64ba8eaf7871904085a9cee1b7789b0e03063d5
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Feb 21 17:58:42 2020 -0500

    Added missing role ansible-bootstrap-python

commit 590ba8e92600271786ee24a5a2eb3b310f601aa8
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Feb 21 17:52:08 2020 -0500

    Removed Python pre-reqs
    
    - These have been moved to a separate role
    - https://github.com/mrlesmithjr/ansible-bootstrap-python.git
    - Only enforced during testing for now and not added as dependency

commit 4cd8db24ecc96f915b588cdfaa32d6af12f0e595
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Feb 21 17:25:59 2020 -0500

    Cleanup and trying to fix Ubuntu 16.04

commit 62309184312769a4294c1525acd3f86fb681ac13
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Feb 21 17:02:51 2020 -0500

    Disabled Fedora testing
    
    - Fedora is failing. Will investigate later.

commit 55c045f85f6da257bb85083ee814fdacb223298c
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Feb 21 16:43:19 2020 -0500

    Changed Molecule scenarios, tests, etc.

commit 07cbbf809bb4ab3da9426d48ddf1eb94f49535cc
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Feb 21 16:43:09 2020 -0500

    Updated files, etc. after new structure

commit 6bcbf5abfa821fced5b9e1e9a10080a5e6dc5c9d
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Feb 19 00:02:45 2020 -0500

    Newly added files from cookiecutter template

commit 37f491fb20f1446d2b9b8c5f439d6f11ebf37e94
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Feb 19 00:02:25 2020 -0500

    Added Debian 10 support

commit 3590c2aa5ec218124c74fe741268927a466bc259
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Feb 19 00:01:53 2020 -0500

    Disabled Fedora for now as it is failing

commit 395740d491231cde8c6a5910e356b392d3f28928
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Feb 19 00:01:39 2020 -0500

    Updated from cookiecutter template

commit f9e37a932664f1b4240a1fae49915841953a1dac
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Feb 19 00:00:50 2020 -0500

    Updated default version

commit 02c215777a646256d7f5cb9912487eea4e391aaa
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Feb 18 23:48:30 2020 -0500

    Removed old files no longer needed

commit a7d7f57f7dcca21543cc49aa9b3343e45ad3418f
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Feb 18 23:46:00 2020 -0500

    Replaced previous testing methods in favor of new Cookiecutter template

commit a58f75726b255eb17b32d3d5ba28de7d912deada
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Dec 28 08:39:59 2018 -0500

    Disabled Ubuntu Trusty

commit d8fb525a8fdc80d0e5902595ddc487f0d6e86a9d
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Dec 28 08:26:31 2018 -0500

    Added wait to ensure port is open before creating dbs

commit 6a43ba91b00059ba457091b1955d7eb106b41963
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Dec 28 01:37:07 2018 -0500

    Fixed incorrect conditional check for Fedora

commit d348bb0e1eba5a10c4e472262bfef772355de8f4
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Dec 28 01:31:44 2018 -0500

    Fixed incorrect Travis CI build status link

commit bee26a8d3eada5cc0cf552dfa6054287dc605a24
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Dec 28 01:11:18 2018 -0500

    First commit of refactoring
    
    Cleaned up code based on Ansible lint and YAML lint
    Implemented updated Travis CI testing

commit 0cc2e74487ed09f24ed0d8337734b4d058fc7999
Author: Paul Houghton <paul4hough@gmail.com>
Date:   Sun Oct 21 14:29:24 2018 -0700

    added validation info

commit e0beee626c572f3cf4eb672ca3e317e6e6e86639
Author: Paul Houghton <paul4hough@gmail.com>
Date:   Sun Oct 21 14:18:53 2018 -0700

    cleanup

commit 85fe0948ba87de73ea11e95dec6839e52f2d0f0f
Author: Paul Houghton <paul4hough@gmail.com>
Date:   Sun Oct 21 14:16:43 2018 -0700

    pass: validate port config changes

commit 8b0f33bdca00a963f2c8f3586f983f5791417cce
Author: Paul Houghton <paul4hough@gmail.com>
Date:   Sun Oct 21 10:48:15 2018 -0700

    restore admin port to 8083

commit 4239bb7011d0f423d993300a7a754f645943f1d4
Author: Paul Houghton <paul4hough@gmail.com>
Date:   Sun Oct 21 09:32:52 2018 -0700

    test with vagrant and testinfra passing

commit c4aa30255bda93612506a237cab9ddd9a0fdb977
Author: Paul Houghton <paul4hough@gmail.com>
Date:   Sun Oct 21 08:36:40 2018 -0700

    tests passing

commit 891f9dfd985991d9892993d439d7ed080c0fb64c
Author: Paul Houghton <paul4hough@gmail.com>
Date:   Sun Oct 21 08:35:58 2018 -0700

    changed sha value for new version

commit b94dbe595570c20b3381f1d04bc7a1b5dcbd42ef
Author: Paul Houghton <paul4hough@gmail.com>
Date:   Sun Oct 21 07:54:44 2018 -0700

    chg influxdb version

commit dd7a430d3d4a91ef6fccc9702d5f5601450a0b02
Author: Paul Houghton <paul4hough@gmail.com>
Date:   Sun Oct 21 07:54:15 2018 -0700

    wip

commit 6e4a7b5d1ba1dbd0ad621db81afd1d32a6870935
Author: Paul Houghton <paul4hough@gmail.com>
Date:   Sun Oct 21 07:33:56 2018 -0700

    wip

commit 982a096c8209453a799a75b24623e475487d6207
Author: Paul Houghton <paul4hough@gmail.com>
Date:   Sun Oct 21 07:32:31 2018 -0700

    gen with molecule init
    
    cmd: molecule init scenario -d vagrant -r influxdb -s default --verifier-name goss

commit ad57150ed1e6d410ae0e1618528da5e9f602619e
Author: Paul Houghton <paul4hough@gmail.com>
Date:   Sun Oct 21 07:27:18 2018 -0700

    yamllint cleanup

commit 1445c373f8923ce6bf5ec28998a88361d30b0b7d
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Dec 30 00:17:02 2017 -0500

    Added Influxdb version

commit 067725364d2d0b418aac24ea3fb03abe049e5c8e
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Dec 30 00:11:59 2017 -0500

    Added license

commit 0a806b2db9c905c2db229896a64c66d0b7eb01cd
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Dec 30 00:11:51 2017 -0500

    Cleaned up vars, tasks, repo info
    
    Cleaned up formatting of vars, tasks, and repo info.

commit ac7dff5a2932a292b985c9dad3ef01262dcd962f
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon May 1 21:24:18 2017 -0400

    Added ability to configure InfluxDB
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit b9dadd4f37c675f742aaa13736e59890d904e185
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Dec 3 22:33:19 2016 -0500

    Addresses issue #4
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit d5f8de860edc804aef9116acf5ddfaee90ef561e
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Oct 20 22:40:11 2016 -0400

    Added retention policies in regards to issue #3
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit e9c79c75db988f1cfa8f203e180e3cd107e9e3b1
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Oct 20 22:15:12 2016 -0400

    Addresses issue #2
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit c64290f45e2cdfb3bdb577cc850b849ce53efbfc
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Oct 20 21:56:54 2016 -0400

    Updated Galaxy info
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit bc8ab5e4462703729cd5a0fd8da86ff8fae64484
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Oct 20 21:54:52 2016 -0400

    Added RedHat support for issue #1
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 4babe51ad330e124d2e0cc1f4911349ce8a9ee9c
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Oct 20 20:54:06 2016 -0400

    first commit
