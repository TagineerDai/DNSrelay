### DNS-Relay

Design a DNS server program,
with the "Domain-IP" list("dnsrelay.txt") loaded in,
and could search the list for IP when the client query with the related domain name.  
There are three possible query answers:
* When the IP is 0.0.0.0, return to the client that "Domain does not exist; please check your spelling." (BAD website interception)
* When the answer is a trival IP, return this address to the client.
* When the answer couldn't be found in the list, query to a foreign DNS server, when get returned, return it to the client. (There could be more than one client, remind of the QueryID)
* Build up some option for debugging.
  + Adding/removing pair.
  + Print all the records in cache/list.
  + Print the query in buffer.
  + Options to change the Dwelling Time of one record in cache.
* Setting a timestamp for cache list.

#### Week1 - TaginDai
+ Data defination.
+ Option defination.  
+ TODO: Receive from Client.
+ TODO: Query with multi-thread.

###### 1. Data defination
* The cache list:                         [DONE]  
  + dict Domain(lowercase)-&gt;IP/Time
  + Time++/Del
  + update/all
  + Search
* The file list:                          [Half-DONE]
  + dict Domain(lowercase)-&gt;IP         
  + I/O                                   
  + Search/get/Set
    - Use The BTrees.OOBTree  
      [pip install btrees]
    - The added rec should be reg vaild   [TODO]

###### 2. Option defination
+ Server                                  [DONE]    
An arg_parser in DNSRelay.py  
These arguments are for initialization.
  * -f &lt;filename&gt;  
Filename of the DomainName-IP list.
  * -t &lt;second(int)&gt;    
The longest dwelling time of one recored in cache.  
(Default: 600second)
  * -c &lt;size(int)&gt;
Cache size.  
(Default: 200 records)
  * -b &lt;size(int)&gt;  
Buffer size;  
(Default: 512 package)
+ Client                                  [TODO]  
  * -c  &lt;IP::Port(string)&gt;
Connected with IP::Port
  * -q &lt;No option&gt;  
Quit   
+ In Client                               [TODO]  
  * -p &lt;c(cache)|f(file)&gt;  
Print all the record in cache/file.  
  * -g &lt;Domain Name&gt;  
Get the corresponding IP for this domain name.  
  * -a  &lt;Domain name&gt; &lt;IP&gt;  
Add a record in the DNSrelay list.
  * -d &lt;Domain name&gt;
Delete the record from DNSrelay list.

DNSrelay --&gt; Client  [reply]

###### 3. Receive from Client
  * Connection setting (net)              [DONE]
    + UDP/IPv4 socket -&gt; local client  
    + receive msg
  * parse msg -&gt; DomainName            [----]
  * Client list
    + IP address
  * Query list  
    + time + URL + cIP
###### 4. Query with multi-thread
* Connection setting (net)                [DONE]
  + UDP/IPv4 socket -&gt; foreign server  
  + UDP/IPv4 socket -&gt; local client
  + local server binding
* multi-thread                            
    + blocking wait & threading           [DONE]
    + query buffer 512                    [TODO]
* building the dgram                      
  + query                                 [TODO]    
  DNSrelay --&gt; net.Foreign
  + reply (send directly)                 [DONE]
  DNSrelay --&gt; net.Client  

#### Week3 - TaginDai
+ A class of Network parameter
+ UDP server [DNS server]
+ UDP foreign query [DNS server]
+ UDP client [DNS user]

##### 1. A class of Network parameter
  + Drop the last two issues in Week1 [TODO]
  + parameter class netparam [TODO]  

##### 2. UDP server [DNS server class]
  + inherent just as the Time Server in python cookbook
    - snedto() // recvfrom()
    - inherent threadUDPserver
##### 3. New multi-thread Client and Server
  + Refer to [this URL](https://gist.github.com/micktwomey/606178).
  + Added settimeout in Client
  + TODO: find how to cancel the binding of socket and addr@port
