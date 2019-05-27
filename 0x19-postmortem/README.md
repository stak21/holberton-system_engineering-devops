__Issue Summary:__

        From 3:00 pm to 5:00 pm, We were getting complaints that our website was slow and on some occasions unable to connect. 
        Most of our users could access our website, but the delay appears to be very disruptive. Our userbase of 50, about 10% were 
        sending in complaints. We could estimate that 100% of our userbase was probably being affected based on our analysis of the 
        monitoring system.

__Timeline:__

        3:00 pm - The first complaint that our website was slow
        3:15 pm - Multiple complaints about a slow down on our website
        3:30 pm - Our support team began relating the issue to the on call site reliability engineer
        3:35 pm - The SRE began investagating the issue and looked into the monitoring server
        3:40 pm - Gave a report of the current situation, the secondary server had crashed and all requests were being sent to the 
                primary server
        4:00 pm - The cause appeared to happen because Sammie our SRE on the previous shift had left a mug of coffee in the server room 
                where the servers were being run There was a small disturbance and the coffee had appeared to spill over the computer that was running our primary server.
        4:05 pm - We had an extra computer where we started up the server using our puppet automation deployment
        4:10 pm - While we waited for the server to run, we got a bag of rice and dumped the laptop in the rice
        4:30 pm - The server is up and running, and appears to be working properly. Doing final tests to make sure everything is good
        5:00 pm - We updated the users that everything is running laptop
__Root cause:__

        The on the day 4/20/2019, our SRE on call Sammie Left some coffee on the desk that had a computer that was running our
        primary server. He had an emergency to go deal with at the hospital. His cat was very ill from possible alcohol poisoning and 
        rushed to the hospital without warning. During his absence, a small tremor  occurred around 2:40 pm and the coffee had been 
        knocked over spilling over the computer. 3 weeks later our users started sending in a report about the site being slow and that
        is when we found out that our primary server has been out for three weeks. Sammie has yet to come back and apparently our backup
        SRE was working remote the entire time and did not notice the problem. We quickly found out where the computer was located and 
        had our SRE redeploy our primary server. In the meantime, we bought a bag of rice and dumped our computer in there to try to save 
        it.
        
__Corrective measures:__

        Have our team be more communicative as to what state our product is in.
        Have all members of the team report that they are having an emergency and state how long they will be gone for
        Have all members work deligently and make sure that our website works properly
        TODO: fire the backup SRE for not checking our site for three weeks while Sammie was gone with his cat
