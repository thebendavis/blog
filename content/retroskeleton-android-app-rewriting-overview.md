title: RetroSkeleton: Automatic Android App Bytecode Rewriting
date: 2015-01-30 20:00
category: research
tags: android, dalvik, mobile
isproject: true
summary: Do you know what your apps are doing? RetroSkeleton is a flexible Android app bytecode rewriting framework that empowers users to observe and control the functionality of the third-party apps.

### Do you know what your apps are doing?

Android is the [most popular mobile platform in the world](https://developer.android.com/about/index.html), and a major reason for this success is the tremendous number of third-party apps available for these devices.
But as amazing as it is to pack these little computers with sensors, fill them with our data, and keep them with us wherever we go, we should consider the risks we take when we run third-party software.
How can we understand and control what third-party apps are doing on our devices?

Most Android apps never undergo a rigorous manual review and the controls provided by the Android platform (primarily the permission system) are quite limited.
Android's permission system requires app developers to declare all permissions (which you can think of as categories of functionality) their app may use.
In order to install an app, the user must grant unlimited access to all permissions requested by the app.
Many important permissions lack granularity.
For example, the `INTERNET` permission enables unlimited connections to any host.
Once the app is installed, the user cannot change, restrict, or revoke the app's ability to perform most sensitive operations.

These are not hypothetical concerns.
For example, when you install an app, Android does not allow you to
prevent a flashlight app from [uploading your personal data and location](http://www.ftc.gov/news-events/press-releases/2013/12/android-flashlight-app-developer-settles-ftc-charges-it-deceived "Android Flashlight App Developer Settles FTC Charges It Deceived Consumers: 'Brightest Flashlight' App Shared Users' Location, Device ID Without Consumers' Knowledge"),
force [apps that make insecure HTTP requests][android-ssl-insecurity] to use (encrypted) HTTPS connections instead,
or apply [workarounds][securerandom-workarounds]
to [platform weaknesses][symantec-securerandom-issue]
that leave [unpatched bitcoin wallet apps vulnerable](https://bitcoin.org/en/alert/2013-08-11-android "Android Security Vulnerability").



### RetroSkeleton gives users control over their apps

At the University of California, Davis, I led a project where my colleagues and I set out to develop a practical way to give users insight into and control over the third-party apps on their Android devices.
We developed RetroSkeleton: an Android app analysis and bytecode rewriting framework for altering the behavior of existing applications without requiring source code or app-specific guidance.
RetroSkeleton rewrites an app to produce a new app that obeys the desired policy.
The foundation of our system is a sophisticated static analysis engine that determines the modifications needed in order to enforce the desired behavior in an app automatically.
We named this app rewriting system RetroSkeleton after the ability to retrofit apps with new behavior by modifying their internals.

We designed our system to be:

* **Complete:** able to intercept all invocations of behavior of interest, including those invoked dynamically (e.g., via reflection)
* **Flexible:** powerful enough to satisfy a wide range of security and functionality goals
* **App-Independent:** no manual app-specific guidance needed to create or apply these transformation policies
* **Deployable:** rewritten apps work on unrooted, unmodified, stock Android devices with no additional software required


### How does it work?

RetroSkeleton allows policy writers to create a single, high-level, app-agnostic policy that RetroSkeleton can apply to any Android app without requiring any manual guidance.
Our system takes as input an app-agnostic policy and applies it to an app automatically by identifying all the necessary transformations and generating all code needed for handlers/dispatch and interposition.
RetroSkeleton parses and rewrites [Android (dex) bytecode](https://source.android.com/devices/tech/dalvik/dex-format.html "Dalvik Executable format") directly (i.e., rather than converting to Java bytecode), replacing all invocations of methods of interest with calls to new handlers with custom behavior, as determined by a policy specification.
Analysis and rewriting is done statically, but generates and inserts handlers that can make policy decisions within the rewritten app at run-time to deal with reflection and other dynamic behavior.
Rewritten apps can run on stock Android devices (no rooting/custom ROMs required).

![RetroSkeleton System Diagram]({filename}/blog_media/2015/retroskeleton/retroskeleton-system-diagram.svg "RetroSkeleton System Diagram")

Users may apply RetroSkeleton to apps they download on their own, either directly or via online service, and corporate environments could require that apps be rewritten before installation on company devices (either on-demand or by providing a private market of rewritten apps).
Because RetroSkeleton policy specifications are app-agnostic, a small set of community-maintained and vetted policies could be used by a wide range of users.

The majority of RetroSkeleton is implemented in [Clojure](http://clojure.org/) and Java, with earlier work implemented in Python.
Please see our publications for details on the design and implementation of our system, as well as the interface policy writers use for policy specification.


### Using RetroSkeleton on real apps

We created a number of policies to showcase the power and flexibility of RetroSkeleton.
Here are some of the behaviors our policies can automatically embed and enforce in Android apps:

* prevent connections to unauthorized hosts via fine-grained network access controls (including user-configurable white/blacklists)
* dynamically replace apps' insecure HTTP requests (a [common problem][android-ssl-insecurity]) with encrypted HTTPS requests when available (a la the [HTTPS-Everywhere][https-everywhere] extensions for browsers)
* perform (rudimentary) app localization by translating app UI text dynamically via online translation services (think "translate this page" for app UI content)
* automatically patch apps with [workarounds][securerandom-workarounds] for [known cryptographic vulnerabilities][symantec-securerandom-issue] in older versions of the Android platform

We applied each of these policies to over 1,000 top free apps from [Google Play](https://play.google.com/store) and built an automated test system to run and exercise each rewritten app in an Android emulator to confirm the functionality of the rewritten apps, including the enforcement of the desired behavior.
Nearly all (more than 97.5%) successfully ran after rewriting (a few threw errors as a result of poorly handling changes in behavior, such as expecting a hardcoded string but receiving the translated version of that string).
For more details, please see our publications below.

For most policies, the impact of the rewriting process on the size and run-time performance of the app is minimal.
On average, rewritten apps increased in size by only a few KiB, which was a less than 0.13% increase in overall app size in our data set.
The specific run-time performance impact depends on the new behavior added, but the inherent overhead of our approach is low, adding only fractions of a microsecond when interposing on method calls of interest (even on aging hardware).
Because much of the work is done statically, generally the impact is not much more than if the developer had originally written the app with the additional behavior.
The static analysis and app rewriting process itself is efficient in terms of time and computation required, averaging about 5 seconds to rewrite an app using normal desktop PC hardware.


### Read more in our publications

Parts of this work have been published in the following peer-reviewed publications with the coauthors named below:

  <span class="bib-entry">
    <span class="papertitle">RetroSkeleton: Retrofitting Android Apps (<a href="/pubs/davis-mobisys13-retroskeleton.pdf">paper</a>, <a href="/pubs/davis-mobisys13-retroskeleton-slides.pdf">slides</a>)</span>
    <span class="author">Benjamin Davis and Hao Chen.</span>
    <span class="venue">11th International Conference on Mobile Systems, Applications and Services (MobiSys). Taipei, Taiwan, June 25-28, 2013.</span>
  </span>

  <span class="bib-entry">
    <span class="papertitle">I-ARM-Droid: A Rewriting Framework for In-App Reference Monitors for Android Applications (<a href="/pubs/davis-most12-iarm.pdf">paper</a>, <a href="/pubs/davis-most12-iarm-slides.pdf">slides</a>)</span>
    <span class="author">Benjamin Davis, Ben Sanders, Armen Khodaverdian, and Hao Chen.</span>
    <span class="venue">IEEE Mobile Security Technologies (MoST). San Francisco, CA, May 24, 2012.</span>
  </span>

For further elaboration, please see my Ph.D. dissertation:

  <span class="bib-entry">
    <span class="papertitle"><a href="/pubs/davis-dissertation.pdf">Protecting Systems from Within:<br />Application-Level Observation and Control Mechanisms</a></span>
    <span class="author">Benjamin Davis, Department of Computer Science, University of California, Davis.</span>
    <span class="venue">Dissertation Committee: Hao Chen, Matthew Bishop, Karl Levitt</span>
  </span>


[android-ssl-insecurity]: http://android-ssl.org/files/p50-fahl.pdf "Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security"
[https-everywhere]: https://www.eff.org/https-everywhere "HTTPS-Everywhere browser extensions"
[securerandom-workarounds]: http://android-developers.blogspot.ie/2013/08/some-securerandom-thoughts.html "Android Developers Blog: Some SecureRandom Thoughts"
[symantec-securerandom-issue]: http://www.symantec.com/connect/blogs/android-cryptographic-issue-may-affect-hundreds-thousands-apps "Android Cryptographic Issue May Affect Hundreds of Thousands of Apps"
