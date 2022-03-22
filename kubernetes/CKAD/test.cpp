#include <bits/stdc++.h>

using namespace std;
struct MessageList {
   std::map<char, char> message;
}
struct EncMessage{
    String timestamp;
    String vcmdb_resource_name;
    String state;
    std::map<char, char> context; //put type of context
    String product_team= "SAN-PHY"
}
void write_health_state_to_cmdb( struct MessageList message_list, cmn_stream){
    /* 
    Publish a message to CMDB, with the VM shortname and the health status
    The health status is a direct mapping from the component status derived
    and 'vm_resource_state_dict' maintained

    Args:
        list of messages (status, fault-code) and producer object

    Returns:
        None

    Exception:
        Raised if the producer was not able to put the message to the databus
    */
    message = message_list.message
    char *ptr;
    ptr = strtok(message['tags']['host'], "."); 
    service_name = *(ptr)
    state = vm_resource_state_dict[int(message['value'])][0]
    context = vm_resource_state_dict[int(message['value'])][1]

    struct EncMessage enc_message;
    enc_message.timestamp = //value
    enc_message.vcmdb_resource_name = service_name
    enc_message.state = state
    enc_message.context = context

    try {
        cmn_stream_producer.put(enc_message)
    } catch (const std::exception& e) {
        log.Fatal('write_health_state_to_cmdb: producer unable to write message to databus')
        exit(1)
    }
}