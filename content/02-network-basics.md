# 🌐 Network Basics

---

## 📌 What is Network?

A network is a group of computers and devices connected together to **share data and resources**.

- Allows communication between systems
- Can be wired (cables) or wireless (Wi-Fi)
- Essential for internet, cloud, and DevOps systems

💡 Every DevOps system relies on networks to function!

---

## 🧭 IP Address

An IP Address is a **unique identifier** for a device on a network.

- Like a home address, but for computers
- Used to send and receive data

### Example:
```
192.168.1.1
```

### Types of IP:
- Public IP → Used on the internet
- Private IP → Used inside local networks

💡 Without IP addresses, devices cannot communicate!

---

## 🏠 LAN (Local Area Network)

A LAN is a network that connects devices in a **small area**.

### Examples:
- Home network
- School or office network

### Characteristics:
- High speed
- Limited geographic area
- Usually privately owned

💡 Your Wi-Fi at home is a LAN!

---

## 🌍 WAN (Wide Area Network)

A WAN connects networks over a **large geographic area**.

### Example:
- The Internet (largest WAN)

### Characteristics:
- Covers cities, countries, or continents
- Slower than LAN (generally)
- Connects multiple LANs together

💡 DevOps systems often run across WANs (cloud infrastructure)

---

## 🌐 HTTP (Hyper Text Transfer Protocol)

HTTP is a protocol used to **transfer data between a web browser and a server**.
- Used when you visit websites
- Works on port 80
- Data is sent in plain text

### Example:
http://example.com


⚠️ Not secure — data can be intercepted

---

## 🔒 HTTPS (Hyper Text Transfer Protocol Secure)

HTTPS is the **secure version of HTTP**.
- Protects sensitive information (passwords, payments)
- Works on port 443

### Example:
https://example.com


💡 Always prefer HTTPS in real applications!

---

## 📦 TCP (Transmission Control Protocol)

TCP is a protocol that ensures **reliable data delivery**.

### Features:
- Data is sent in order
- Errors are checked and corrected
- Guarantees delivery

### Use Cases:
- Web browsing
- File transfers

💡 Think of TCP like a **tracked delivery service**

---

## ⚡ UDP (User Datagram Protocol)

UDP is a protocol that sends data **faster but without guarantees**.

### Features:
- No error checking
- No delivery confirmation
- Faster than TCP

### Use Cases:
- Video streaming
- Online gaming

💡 Think of UDP like a **regular mail service (fast but no tracking)**

---

## 🔄 TCP vs UDP

| Feature | TCP | UDP |
|--------|-----|-----|
| Speed | Slower | Faster |
| Reliability | High | Low |
| Error Checking | Yes | No |
| Use Cases | Websites, APIs | Streaming, gaming |

---

## 🚀 Summary

- Networks connect devices for communication
- IP addresses identify devices
- LAN = small networks, WAN = large networks
- HTTP/HTTPS handle web communication
- TCP = reliable, UDP = fast

---

## 🎯 Key Takeaway

👉 Networking is the **foundation of DevOps**, because all systems, services, and tools communicate over networks