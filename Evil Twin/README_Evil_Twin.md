# Evil Twin Scenario
## 1. Introduction
This project targets the replication of potential threats in 5G networks, specifically focusing on the Evil Twin attack. By leveraging MITRE FiGHT scenario mapping, we aim to develop effective methods to detect and understand these cyber threats within 5G systems. The project utilizes a mix of theoretical research, hands-on experiments, and proven techniques from the MITRE FiGHT framework to identify threats and enhance security research for 5G and beyond, into 6G technologies.

For more details on the configuration file, please visit our [GitHub](https://github.com/cypheriumv/Threat_Hunting_on_5G_Future_Communication_Testbed_Using_MITRE_FiGHT_Framework) repository. You can also view detailed logs of the NGAP packets and a demonstration video on the team’s [Google drive](https://drive.google.com/drive/folders/1DsDQewa0rqMWj2y-lWif3s2mAYYdu7kJ?usp=sharing), giving you a clear look at our work and how effective our methods are against these attacks. This project aims to make 5G networks stronger and safer from sophisticated attacks like Evil Twin.

## 2. 	Objective
The primary objective of this project is to establish a 5G simulation environment that acts as an Evil Twin access point, using a gNodeB setup. This simulated environment will replicate a legitimate 5G network node but operate as a rogue node to intercept mobile device communications. Key goals include:

1. **Setup and Configuration**: Establish a gNodeB to mimic a legitimate 5G access point. This setup involves configuring the gNodeB to broadcast a network signal that appears as a genuine 5G network to devices, enticing them to connect.
2. **Device Connection and Data Capture**: Once devices connect to the rogue AP, facilitated by the gNodeB, their data traffic, including internet requests and transmitted packets, will be routed through the rogue system. This allows for capturing and analyzing the data packets transmitted by these devices.
3. **Sim Card Registration**: Implement a system that allows 5G SIM cards to register with the gNodeB, thereby authenticating it as part of the network. This step is crucial for the gNodeB to appear as a legitimate network node to the devices.
4. **Threat Analysis and Mitigation Development**: Analyze the captured data to identify potential security vulnerabilities and attack vectors. Develop mitigation strategies to protect against such vulnerabilities in real-world scenarios.
5. **Documentation and Knowledge Sharing**: Document all findings, configurations, and outcomes from the project. Share these insights through comprehensive logs, reports, and demonstrations to contribute to broader cybersecurity knowledge and defenses.


This project's ultimate goal is to enhance the security measures in 5G networks by demonstrating the feasibility and risk of Evil Twin attacks and developing robust defenses against them. By simulating these attacks in a controlled environment, we aim to prepare better network operators and security professionals to detect, respond to, and mitigate such threats effectively.
