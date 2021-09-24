import streamlit as st
import datetime

st.markdown("<h1 style='text-align: center; color: black;'>Streamlit Cover Letter</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: black;'>Fred Zimmerman</h2>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: black;'>wfzimmerman@gmail.com | +1.734-545-5369</p>", unsafe_allow_html=True)


st.markdown("<p style='text-align: right; color: black;'>September 24, 2021</p>", unsafe_allow_html=True)

st.markdown("""When I first saw Streamlit, two weeks ago, I had three main reactions over the course of the first twenty-four hours. 
- "This is amazing, why haven't I seen this before."
- "This is ideally suited for my work in bringing data science to the world of book-lovers." 
 -  "I am going to scrap all my other stuff and bring everything together in this framework."
 """)

st.markdown("""I am a serial entrepreneur, developer, and product manager with experience with big data in the climate, legal, intelligence, and publishing industries.  I graduated from Swarthmore College and have a JD from Wayne State University Law School. In a diverse career at the intersection of tech and publishing, I have been a data archivist for a NASA contract, a product manager for LexisNexis and the publishing company Gale, an intelligence analyst for US government, done an angel-funded startup, and created a publishing company.""")

st.markdown("""My publishing company, Nimble Books, has a variety of digital assets built up over the course of 15 years, including a Ghost blog, a pile of static html pages, a Flask/Stripe-based suite of tools for book-lovers using OpenAI (with a React v2 in progress), a royalty program using Pandas, and lots of offline content in spreadsheet, docx, PDF, image, and archival JSON formats.""")

st.markdown("""Finally--finally--here was a platform that I could use to integrate *all* my data, and bring it _all_ together in a way that I could use to make a better world for book-lovers.  I sprang into action exploring the Streamlit system and within two weeks was able to stand up a [new version of my publishing website](http://www.NimbleBooks.com) using the Hydralit multi-page app and including dataframe, text, OpenAI, and json content.""")

st.markdown("""As I explored, I observed that there are open positions at Streamlit. I love that you are remote-first, as it gives me an opportunity to arbitrage my strong skill set among a much wider set of options; while there is a healthy startup economy in Ann Arbor, it's just not that big. I also like your value statement, which fits me well, and that you are seed-stage and growing rapidly. I think I might fit well for either of the two open Product Manager positions, but I leave it to you to determine which might be a better fit.""")

st.markdown("""Let me first comment on the Ecosystem position.  I am quite familiar with the Flask ecosystem, having built several dozen Flask apps over the last five years, and I was in the middle of teaching myself React when I saw Streamlit. I see from your launch blog that your founders were grappling with the exact same Flask/React spaghetti that made me eager to explore Streamlit. From my knowledge of Flask/React (and other platforms from the paleo era, like WordPress) I can see that there are a lot of known missing pieces in the Streamlit ecosystem--for example, most of the extensions needed to support a SAAS startup are either minimally supported or not present at all. I can see some of the tools beginning to emerge and I see others on the roadmap.  I think one important strategic question is horizontal--what are the types of extension that will benefit almost any user type? Analytics and monetization are obvious examples.  The complementary strategic question is vertical--what are the "target" ecosystems whose user tasks you want to be sure are supported? I am sure you already have lots of ideas about which verticals to go after, so I'll just make a couple of observations based on my own experience.""")

st.markdown("""- The US intelligence community is always a good target for venture-funded data science companies. A secure-able version of Streamlit would be especially powerful to the IC because it is full of small teams of only a very few smart people working on hard problems. People on these teams have access to a wealth of data, but getting agency IT to build something for them is, to put it mildly, not easy. Data exploration and visualization are super important to these people because their ultimate end users are mid-grade and senior policy makers who consume briefings, not documents and not data. If this market is of active interest, it's worth mentioning that I have had high security clearances (TS/TK/SCI/H) that could be reactivated.""")

st.markdown("""- Similarly, climate science is a domain full of small teams who crunch big data and who have a pressing need to communicate rapidly and visually with policy makers and the public.  As with the IC, ecosystem features that made it easier for teams to share data with one another would be very valuable.""")

st.markdown("""- Scientific publishing is more hierarchical and more focused around huge data warehouses, but it's an area that fits nicely with your core audience's interests and needs. The scientific publishing companies are always looking for ways to go beyond the PDF journal article. Alternatively, a way to press a button and create an open access journal in Streamlit integrated with SciHub would probably be pretty popular!""")

st.markdown("""In short, I think I understand the needs for ecosystem development reasonably well and have the diverse skill set needed to deal with a wide variety of developers and user tasks.""")

st.markdown("""Next a few thoughts on the Magic apps position. """)

st.markdown("""I am still getting familiar with the Magic features, but as I understand it from looking at the github code, a key aspect is that you are rewriting the Python Abstract Syntax Tree on the fly to eliminate a lot of boilerplate code.  I am a participant in OpenAI's Codex private beta (as well as GitHub copilot) and it's clear that the world is moving rapidly towards a sort of push-button wish fulfillment for creating program functions.  That fits well with what Streamlit is already good at. An integration there would be a quick win, and I suspect many other alternatives are likely to arise.""")

st.markdown("""I believe the bigger challenges, and therefore the bigger opportunities for 10x 'Magic' features, are in figuring out ways to give individual data scientists the ability to compete with the data collection and processing "moats" that surround large organizations. For example on the collection side, in a domain I know well, book publishing, a couple of big companies have huge advantages in terms of their access to large corpora of book.  How is the individual or small team to compete with Amazon or Google's access to millions of digitized books that they acquired through mechanisms that, were, frankly, barely legal? People in universities can sometimes get lesser levels of access through programs like HathiTrust or through noncommercial collaboration, but that's not good enough.  The same situation applies in other industries, of course, where a handful of big companies control crucial troves of data in social networks, media, location, and so on.  On the processing side, too, when the competition is among huge companies building trillion-parameter models, it can be daunting for individual data scientists to secure comparable resources.""")

st.markdown("""So I would argue that one obvious opportunity for 'magic' is to somehow radically improve individual data scientists' ability to collect and process large data sets, and I would add the requirement that to be 'magic', it should not be dependent on the goodwill of the FAANG companies or any national government. ;-) 

The following is just an example chosen at random from a couple of things that I read recently, and is not meant in any way to suggest a lack of openness to other opportunities for 'magic.' In [a recent exchange on Twitter, the futurist John Robb discussed his recent testimony to Congress](https://twitter.com/johnrobb/status/1440434304899694599?s=20) where he made two major points:


>1) Data ownership.  You own your data, you should be in control of it.
>2) Digital rights. Rights that protect us against a corporate-run surveillance state (there are none right now).

>If we had #dataownership and there were firms in this hearing today that were actively operating as advisors, advocates, and managers of our data... we would have been talking about instances of improvement rather than repeated instances of abuse.

I responded to John and observed that I do not think that creating a sixth FAANG company would necessarily have the hoped-for benefits. I pointed out there are already billions of dollars invested in data decentralization via blockchain and directed him to Balaji Srinivasan.  Balaji replied with a link to [this article](https://balajis.com/yes-you-may-need-a-blockchain/) where he presents a pleasingly specific discussion of existing data interchange formats -- he lists APIs, JSON, PDF, CSV, MBOX, and/or SFTP -- and argues that the next big step forward is to have people able to treat public blockchains as "massively multiclient open state databases where every user is a root user." Now, I'm not a religious enthusiast about blockchain or bitcoin, but I can see where's he's heading with this, and where having data scientists using be able to read and write to a MMOODB _as easily as JSON_ might be a bit of transformational 'magic.'

To repeat, this is just an example--I would expect the PM for Magic to be having lots of conversations like this, including many that are much more technically-focused--but I hope this gives a flavor for my pre-context approach to the role.

I trust this adequately communicates that I would bring to Streamlit a high level of passion, energy, and alignment with a shared vision.  I would very much enjoy meeting some members of your team and learning more about your future direction.

Cordially,

Fred Zimmerman
""")

