title: Deft note-taking: the power of plain text
date: 2015-02-27 20:00
category: workflow
tags: emacs, markdown, dropbox, ios
summary: My rock-solid keep-it-simple system for searching and editing all of your notes.


### A filing cabinet of post-it notes

I keep tons of little notes - information that I may not use frequently, isn't part of a bigger project, but might be useful later.

For example:

* "cheat sheets" for infrequently-used software and tools
* the steps I took to perform a complex configuration/setup task, and resolutions to cryptic errors that were difficult to diagnose
* notes from books I've read
* notes from workshops, presentations, and meetings not associated with a bigger project
* lots of lists: gift ideas for friends and family, my travel/packing list, organizations I need to contact with my updated address when I move, and many more

When in doubt, I'll save it in a note.
This has saved me dozens of times:

* Weird workaround when setting up the server? Guess who saves the day (hours, at least) 18 months later when we get a new server and need to set it up the same way.
* "Wasn't there a guest speaker last year who talked about something like this?" Indeed there was - here are my notes about her presentation.
* "I think we looked into this but decided it was a dead end. Do you remember why?" Here are the technical limitations we hit.
* "Wait, what did we get him for last Christmas?" I have the list right here.

I use a system based on [markdown][]-formatted plain text files, accessed using [Deft][deft] for Emacs, and synced via Dropbox.
It's served me well for years, particularly in grad school when I was constantly exploring new ideas and performing experiments.
Here's a little about the why and how.


### Sustainable note-taking

Ever spend an afternoon trying out some new software with a bunch of fancy knobs to turn, only to find it's not worth the hassle?
I wanted a note-taking system that is not only useful, but one I actually use enough to be worth the effort of maintaining.
If I have something to save, I want one trusted place to put it - and if I want to find something, I want one trusted place to look.

Here are my requirements for a note-taking system:

* Notes should be **easy to write**. If adding or editing a note is slow, cumbersome, or requires many decisions, I'm less likely to do it.
* Notes should be **easy to read**. Notes should be fast and simple to access, ideally across platforms. Furthermore, my data should be easy to export and migrate. Services will close and software will rot, and I don't want to lose my notes when this happens.
* Notes should be **easy to find**. I need a good search system - fast and complete.

I explored a number of options: proprietary and open-source applications, online services, personal wikis...
During these experiments, I came up with a few additional requirements:

* Easy to back up and restore individual notes
* Resilient to changes in note-taking software and variances in implementations (especially across platforms)
* Ability to access and edit notes while offline
* Easy to keep in sync across devices - the less I have to think about this, the better. Merge conflicts are a bummer, but out-of-sync binary blobs are worse.
* Not too "fiddly" - I found tagging/categorizing/cross-referencing notes was a time-sponge and rarely worth the effort. I'd just end up searching anyway.


### The power of plain text

Ultimately I settled on plain text files, one file per note, all in a single directory, with the title of the note as the file name.
This meets my requirements pretty well:

* Text files are fast and easy to create and edit in just about any editor.
* Search is DIY but straightforward. Even `grep` can be used in a pinch, and at least `grep` is fast, reliable, and complete.
* Backups are straightforward, and it'd be hard to be more resilient to software changes.
* I keep my notes folder in Dropbox (I keep sensitive data elsewhere), and sync has worked well for me.
* Dropbox leaves files on the hard drive, so notes are available offline and are included in my system backups.
* Since I'm not dependent on Dropbox for anything other than pushing my data around, the day it stops working I can replace it with something else. I used [Unison](http://www.cis.upenn.edu/~bcpierce/unison/) before Dropbox.

In the content of the note files, I write in [markdown][], which is a lightweight plain text format that is designed to be easy to read and write.
Markdown files are plain text and look like this:

    :::text
    # Simple syntax

    Headings start with the # character.
    Unordered lists look like this:

    * alpha
    * bravo
    * charlie

    # Links

    Links can use [inline](http://example.com)
    or [reference style][xyz] syntax.

    [xyz]: http://example.net

Markdown was originally designed for writing content that gets exported to HTML, but I rarely export my notes.
For me, following the markdown syntax just gives me a uniform format that is simple to write and easy to skim.
I also use markdown in other settings (like writing these blog posts), so it's familiar.
I keep [multimarkdown](http://fletcherpenney.net/multimarkdown/) installed on my workstations for other purposes, so it is available on the occasion that I want to export a note to HTML, PDF, or RTF.

There are a few downsides with plain text notes:

* No attachments or fancy metadata. In practice, this hasn't been a big problem for me. By the time I'm creating substantial artifacts for a project, I've probably already set up a git repo or [Trello](https://trello.com/) board or something for the project.
* Typesetting math isn't very elegant. You can write equations as LaTeX or something, but it's not ideal.
* No built-in sharing. You can mix-and-match whatever works for you (git repo, shared directory/drive, etc.) but you have to do it yourself.
* No built-in security mechanisms (e.g., encryption). If you don't trust Dropbox with your notes, you'll have to do something else to sync, like keeping files in an encrypted volume or on a USB stick you can keep with you.


### Wrangling plain text files...

The great thing about plain text is you don't need anything special to read or write.
However, you can make it easier to do common things.

I'm a big fan of the search-first design I first saw in a Mac app called [Notational Velocity](http://notational.net/).
The top two bullet points on the app description page are:

* "**Modeless Operation**: Searching for notes is not a separate action; rather, it is the primary interface."
* "**Incremental Search**: Searching encompasses all notes' content and occurs instantly with each key pressed."

I'm a big fan of this approach - just open and the app searches your notes incrementally as you type.
Sorting notes by most-recently-edited makes frequently-used notes even easier to find.


#### ... on a workstation

I like Notational Velocity (and [nvALT](http://brettterpstra.com/projects/nvalt/), a popular fork), but I'm not always on a Mac so I need something I can use across all of my machines (Linux/Mac/Windows).

Vim is great and use it regularly, but Emacs has become my go-to editor for most things (mostly because I'd rather write elisp than vimscript).
Since I use Emacs everywhere (including the terminal and over SSH), I looked at a number of Emacs-based options.
My favorite is [Deft][deft]: a brilliant Emacs mode inspired by Notational Velocity, featuring the same search-first design.
I use the [Emacs Server](https://www.gnu.org/software/emacs/manual/html_node/emacs/Emacs-Server.html) to keep Emacs running, so launching a new `emacsclient` is very fast, and my notes are just a single keystroke away.
I enable `markdown-mode` for my deft notes, and a few other settings, in [my .emacs.d config on github](https://github.com/thebendavis/.emacs.d).

##### A side note:

If you've already invested in Emacs, definitely check out [org mode](http://orgmode.org/), which has many more powerful features built on a plain-text system.
It goes way beyond markdown's features, including support for time tracking, task and project planning, scheduling, text-based spreadsheets (?!) and more.
Org mode works best when you can put everything into that system, which wasn't a good fit for my setting, but it's worth checking out to see if it works for you.


#### ... on iOS

While I do most of my work on a desktop/laptop, it is useful to be able to quickly search and edit notes on a mobile device.
There are many mobile note-taking apps that sync with markdown files in a Dropbox folder.
On iOS, I've been using [Byword](http://bywordapp.com/ios), which has markdown support and the same incremental search features.


### Keep it simple

I can't tell you how many times I've saved hours of work and frustration by finding a note I wrote years earlier.
But it would have never been there if I didn't have a near-frictionless way to add, search, and maintain my notes.
Simplicity is a feature that led me to an approach that's a bit DIY, but flexible and within my own control.
Out of all of the note-taking apps and services available five years ago, not every option would have left me with an upgrade path of "continue to use whatever text editor you like" to get me to today.
Find a system that works for you, but if you're trying to decide, it's worth thinking five years ahead before signing up for the latest (ad-supported?) note-taking-in-the-cloud service...


[deft]: http://jblevins.org/projects/deft/
[markdown]: http://daringfireball.net/projects/markdown/
