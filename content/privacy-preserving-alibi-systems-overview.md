title: Privacy-Preserving Alibis for Mobile Device Users
date: 2015-02-15 20:00
category: research
tags: crypto, privacy, mobile
summary: How can we use our mobile devices to show where we've been without letting anyone track us?


### Can you prove what you did last summer?

A man faced the death penalty when he was charged with the murder of a government witness.
Months after his arrest, the defense obtained the public transit records associated with the man's MetroCard and found that these records supported his claim that he was miles away at the time of the crime.
After seeing this new evidence, the prosecution [dropped all charges][nyt-metrocard-alibi].

Just imagine what might have happened if this man hadn't used his MetroCard that night.
Cases like this show that while it doesn't happen often, it can be incredibly important to have an alibi.
The tricky part is that you generally won't know when you'll need one before it's too late to get one - if you don't have one already, you're out of luck.
What can we do to make sure we have an alibi whenever we need one?


### Travel like no one is watching

Inspired by the [alibi defense](https://en.wikipedia.org/wiki/Alibi) in criminal procedures, here I'll be using the word "alibi" refer to the general notion of providing evidence to support a claim of having been at a particular place at a particular time.

We can't always count on having used our MetroCard at a critical time.
We should proactively establish alibis whenever possible in order to maximize our chances of having an alibi when we need one - ideally without requiring too much thought or impact on our daily behavior.

With the rise of modern smart phones, it is increasingly common to carry a mobile device with GPS and other location-based sensors wherever we go.
It seems like we should be able to use our mobile phones to establish "alibi" evidence for ourselves in the same way a MetroCard can serve this purpose.

Indeed, there are many apps and services that track the location of mobile devices by having the device periodically upload its location to a centralized server.
The biggest problem with this approach is the lack of control the user has over their privacy - they must trust the third-party service completely with their personal location data.

Furthermore, if users want to avoid revealing their location to the service when doing something they wish to keep private they must decide to turn off the service ahead of time.
This requires making manual decisions with potentially serious privacy implications, and once these decisions are made there is no going back.
Imagine an employee turning off their tracking service when taking a long lunch, later accused of robbing a bank at that time - they're out of luck!

Is there a way to have the best of both worlds?
We'd like to make sure we always have an alibi when we need it, without relying on a third-party to track us and hope they don't do anything creepy - or that nobody creepy gets access to the third-party service's data!


### Privacy-Preserving Alibi Systems

At UC Davis, I led a project with the goal of developing a way for mobile device users to make sure they have alibis when they need one in a way that doesn't require them to give up their privacy.
Our insight was that while you must reveal your identity when you *claim* an alibi, we can construct a scheme where *creating* the alibi does not reveal your identity.

In our system, a user's mobile device runs an app that automatically participates in opportunistic exchanges with nearby devices, creating alibis for the **alibi owner** in a way that does not reveal the identity of the alibi owner.
Essentially, this establishes a "testimony" that the other participant (the **alibi corroborator**) observed the alibi owner (really, their mobile device and a computation requiring the owner's private key) at their current, shared location and time.
The alibi owner stores this testimony for later.

If and only if the alibi owner wishes to claim that particular alibi, they can provide the testimony and some additional information to a **judge** who can verify that the identity associated with the testimony does indeed match the alibi owner (and a number of other properties needed to detect various types of fraud and perjury).
This reveals no other information about any other alibis created by that user, so the user can disclose only what they want, and exactly what they want.
We require no trusted third party to create alibis or provide the security guarantees, and there is no third party that can force a reveal of the identity of alibis without the owner's participation.

Specifically, we created two cryptographic schemes that allow a user's mobile device to opportunistically and automatically establish evidence to support claims of past locations ("alibis") on the user's behalf without revealing the user's identity.
These schemes bind the user's identity to an alibi when the alibi is created, but the identity is only revealed if and when the owner claims the alibi, leaving the user in complete control of the disclosure of their identity.
Our constructions are based on a string commitment scheme that is secure in the unbound receiver model.
These schemes are designed to work within the existing infrastructure available to mobile device users, and do not require additional or existing trusted third parties to fulfill the privacy guarantees of our schemes.


### Design, implementation, and real-world feasibility

Please see the slides from my ASIACCS 2012 presentation for the general flow of the protocols, and the publications for details on the design and implementation of our cryptographic schemes.

We have implemented the computational components of our schemes in an Android app that demonstrates that our approach is feasible for use on mobile devices, in terms of both computation and storage requirements.
The computations required for creating and verifying alibis can be done on even older Android devices in fractions of a second, and only require a few hundred bytes of storage for each alibi created.


### Comparison to traditional alibis

The alibis in our system have much in common with the types of "traditional alibis" normally found in criminal proceedings.
The strength of a traditional alibi depends on the reliability of the evidence and trustworthiness of the corroborator, and the same applies to our alibis.
Just as in the traditional setting, we cannot prevent alibi owners and corroborators from colluding to create a fake but valid alibi (perjury), so in both cases the evaluation of the strength of the alibi is up to the judge to consider the circumstances and context.

However, the alibis in our systems have a number of advantages over traditional alibis.
Primarily, the privacy guarantees discussed above allow participants to create alibis without revealing their identity.
Their identity is only revealed to be associated with an alibi if they themselves decide to claim that alibi, which they can do without revealing anything else about other alibis they have created.
Also, our alibis cannot be created without the consent and participation of the alibi owner.

Furthermore, our alibis have non-forgeability properties beyond that of many traditional alibis, including the ability to reveal one-sided forgeries, where either the alibi owner or corroborator attempts to counterfeit or modify an existing alibi without the other party's explicit, intentional participation.

The identities of the participants are directly and unambiguously embedded into the alibis, preventing the common problem in traditional alibis where imperfect human observation and faulty human memory can result in inaccurate alibi testimony.

We have designed our schemes so the alibi owner stores all data necessary to corroborate and verify the alibi, as they have the greatest incentive to do so.
Unlike many traditional alibis, our alibis do not rely on the memory of the corroborator after alibi creation.

Our papers detail the precise threat model, assumptions, properties and guarantees of our systems, including the safeguards and checks that prevent various types of fraud and perjury.


### Read more in these publications

Parts of this work have been published in the following peer-reviewed publication:

  <span class="bib-entry">
    <span class="papertitle">Privacy-Preserving Alibi Systems (<a href="/pubs/davis-asiaccs12-alibis.pdf">paper</a>, <a href="/pubs/davis-asiaccs12-alibis-slides.pdf">slides</a>)</span>
    <span class="author">Benjamin Davis, Hao Chen, and Matthew Franklin.</span>
    <span class="venue">7th ACM Symposium on Information, Computer and Communications Security (ASIACCS). Seoul, South Korea, May 1-3, 2012.</span>
  </span>

For further elaboration, please see my Ph.D. dissertation:

  <span class="bib-entry">
    <span class="papertitle"><a href="/pubs/davis-dissertation.pdf">Protecting Systems from Within:<br />Application-Level Observation and Control Mechanisms</a></span>
    <span class="author">Benjamin Davis, Department of Computer Science, University of California, Davis.</span>
    <span class="venue">Dissertation Committee: Hao Chen, Matthew Bishop, Karl Levitt</span>
  </span>


[nyt-metrocard-alibi]: http://www.nytimes.com/2009/01/01/nyregion/01murder.html "Murder Case Dropped After MetroCard Verifies Alibi"
