/* Software License Agreement (BSD License)
 *
 * Copyright (c) 2011, Willow Garage, Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 *  * Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *  * Redistributions in binary form must reproduce the above
 *    copyright notice, this list of conditions and the following
 *    disclaimer in the documentation and/or other materials provided
 *    with the distribution.
 *  * Neither the name of Willow Garage, Inc. nor the names of its
 *    contributors may be used to endorse or promote products derived
 *    from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 * FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 * ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 *
 * Auto-generated by genmsg_cpp from file /home/rosuser/ros_workspace/src/fw_wrapper/srv/allcmd.srv
 *
 */


#ifndef FW_WRAPPER_MESSAGE_ALLCMDRESPONSE_H
#define FW_WRAPPER_MESSAGE_ALLCMDRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace fw_wrapper
{
template <class ContainerAllocator>
struct allcmdResponse_
{
  typedef allcmdResponse_<ContainerAllocator> Type;

  allcmdResponse_()
    : val(0)  {
    }
  allcmdResponse_(const ContainerAllocator& _alloc)
    : val(0)  {
    }



   typedef int16_t _val_type;
  _val_type val;




  typedef boost::shared_ptr< ::fw_wrapper::allcmdResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::fw_wrapper::allcmdResponse_<ContainerAllocator> const> ConstPtr;

}; // struct allcmdResponse_

typedef ::fw_wrapper::allcmdResponse_<std::allocator<void> > allcmdResponse;

typedef boost::shared_ptr< ::fw_wrapper::allcmdResponse > allcmdResponsePtr;
typedef boost::shared_ptr< ::fw_wrapper::allcmdResponse const> allcmdResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::fw_wrapper::allcmdResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::fw_wrapper::allcmdResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace fw_wrapper

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'fw_wrapper': ['/home/rosuser/ros_workspace/src/fw_wrapper/msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::fw_wrapper::allcmdResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::fw_wrapper::allcmdResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::fw_wrapper::allcmdResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::fw_wrapper::allcmdResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::fw_wrapper::allcmdResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::fw_wrapper::allcmdResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::fw_wrapper::allcmdResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "eb550c147d284de944354d9ed4deccf8";
  }

  static const char* value(const ::fw_wrapper::allcmdResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xeb550c147d284de9ULL;
  static const uint64_t static_value2 = 0x44354d9ed4deccf8ULL;
};

template<class ContainerAllocator>
struct DataType< ::fw_wrapper::allcmdResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "fw_wrapper/allcmdResponse";
  }

  static const char* value(const ::fw_wrapper::allcmdResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::fw_wrapper::allcmdResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int16 val\n\
\n\
";
  }

  static const char* value(const ::fw_wrapper::allcmdResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::fw_wrapper::allcmdResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.val);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct allcmdResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::fw_wrapper::allcmdResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::fw_wrapper::allcmdResponse_<ContainerAllocator>& v)
  {
    s << indent << "val: ";
    Printer<int16_t>::stream(s, indent + "  ", v.val);
  }
};

} // namespace message_operations
} // namespace ros

#endif // FW_WRAPPER_MESSAGE_ALLCMDRESPONSE_H
