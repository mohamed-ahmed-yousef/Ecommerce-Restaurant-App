import MainComponent from "./MainComponent"
import DropDown from "./DropDown"
import DividerMessage from "./DividerMessage"
import { Icon1, Icon2, Icon3, Icon4, Icon5, Icon6, Icon7, Icon8, Icon9} from './Icons';
import SearchBar from "./Search";
import { Divider } from "@mui/material";
import { useEffect, useState } from "react";
import React from 'react'

const SideBarData = ({open}) => {

    let SideBarItems = [        
        // 1st
        <MainComponent content={['DashBoard']} Icon = {Icon1}  open = {open} />,
        <DropDown main = "pos" nested  = {["New Sale", "Orders"]} Icon = {Icon1[1]} isOpen = {open}/>,
        <DividerMessage message = "ORDER MANAGEMENT" isOpen = {open} />,
        
        // 2nd
        <DropDown main = "Order" nested  = {["All", "Pending", "Confirmed", "Processing", "Out For Delivery" ,
        "Delivered", "Returned", "Failed To Deliver", "Canceled", "Scheduled"]} Icon = {Icon2[0]} isOpen = {open}/>,
        <DropDown main = "Table Order" nested = {["All", "Confirmed", "Cooking", "Ready For Serve", "Completed", "Cancelled", "On Table"]} Icon = {Icon2[1]} isOpen={open}/>,
        
        // 3rd
        <DividerMessage message = "PRODUCT MANAGEMENT" isOpen = {open} />,
        <DropDown main = "Category Setup" nested  = {["Category", "sub Category"]} Icon = {Icon3[0]} isOpen = {open}/>,
        <DropDown main = "Product Setup" nested  = {["Product Attributes", "Product Addon", "Product Add", "Product List", "Bulk Import", "Bulk Export", "Product Reviews"]} Icon = {Icon3[1]} isOpen = {open}/>,
        
        // 4th
        <DividerMessage message = "PROMOTION MANAGEMENT" isOpen = {open} />,
        <MainComponent content={['Banner', 'Coupon', "Send Notification"]} Icon = {Icon4}  open = {open} />,
        
        // 5th
        <DividerMessage message = "HELP & SUPPORT SECTION" isOpen = {open} />,
        <MainComponent content={["Message"]} Icon = {Icon5}  open = {open} />,
        
        // 6h
        <DividerMessage message = "REPORT AND ANALYTICS" isOpen = {open} />,
        <MainComponent content={['Earning Report', 'Order Report', "DeliveryMan Report", "Product Report", "Sale Report"]} Icon = {Icon6}  open = {open} />,
        
        // 7th
        <DividerMessage message = "USER MANAGEMENT" isOpen = {open} />,
        <DropDown main = "Customer" nested  = {["List", "Settings"]} Icon = {Icon7[0]} isOpen = {open}/>,
        <DropDown main = "Customer Wallet" nested  = {["Add Fund", "Report"]} Icon = {Icon7[1]} isOpen = {open}/>,
        <DropDown main = "Custome Loyalty Point" nested  = {["Report"]} Icon = {Icon7[2]} isOpen = {open}/>,
        <MainComponent content={["Subscribed Emails"]} Icon = {[Icon7[3]]}  open = {open} />,
        <DropDown main = "Deliveryman" nested  = {["Delivery Man List", "Add New Delivery man",  "New Joining Request", "Delivery Man Reviews"]} Icon = {Icon7[4]} isOpen = {open}/>,
        <DropDown main = "employees" nested  = {["Employees Role Setup", 
        <DropDown main = "Employee Setup" nested  = {["Add New", "List"]} Icon = {Icon7[4]} isOpen = {open} />] } Icon = {Icon7[5]} isOpen = {open} special={true}/>,
        <DropDown main = "chef" nested  = {["Add New", "List"]} Icon = {Icon7[6]} isOpen = {open}/>,
        
        // 8th
        <DividerMessage message = "TABLE SECTION" isOpen = {open} />,
        <DropDown main = "table" nested  = {["List", "Availability","Promotion Setup"]} Icon = {Icon8} isOpen = {open}/>,
        
        // 9th
        <DividerMessage message = "USER MANAGEMENT" isOpen = {open} />,
        <MainComponent content={["Busineess Setup"]} Icon = {[Icon9[0]]}  open = {open} />,
        <DropDown main = "Branch Setup" nested  = {["Add New","List"]} Icon = {Icon9[1]} isOpen = {open}/>,
        <DropDown main = "Page Media" nested  = {["Page SetUp","Social Media"]} Icon = {Icon9[2]} isOpen = {open}/>,
        <MainComponent content={["3rd Party", "System Setup"]} Icon = {Icon9.slice(3,)}  open = {open} />
        
        ]
        const [isFiltered, setIsFiltered] = useState(false)
        const [filterReuslt, setFilterResult] = useState(null)
        
        const FilterSearch = (value) => {
                setIsFiltered(true)
                var filteredItem = []

                SideBarItems.filter((item) => {
                    if (item.props.content) {
                        const newContent = item.props.content.filter((content) => {
                            return content.toLowerCase().includes(value.toLowerCase());
                        });
                        if (newContent.length > 0) {
                                filteredItem.push({ ...item, props: { ...item.props, content: newContent } });
                        }
                    }
                    else  {
                        const newContent1 = item.props.main
                        var newContent2 = item.props.nested

                        if (newContent2) {
                            const allContent =  item.props.nested
                            // if (allContent.at(-1) !== newContent1)
                            //     allContent.push(newContent1)

                            const newContent = allContent.filter(content => {
                                // console.log(typeof content, content);
                                if(typeof content === "string")
                                    return content.toLowerCase().includes(value.toLowerCase())
                                
                                var inner = content.props.nested
                                // console.log(inner,allContent);
                                // if (inner.at(-1) !== content.props.main)    
                                //     inner.push(content.props.main)
                                inner.filter(innerContent => {
                                    return innerContent.toLowerCase().includes(value.toLowerCase())
                                })
                            })
                            console.log(newContent);
                            if(newContent.length > 0)
                                filteredItem.push({...item, props:{...item.props, content:newContent}})
                        }
                    }
                });
                
            setFilterResult(filteredItem)
          };

  return (
    <div>
        <Divider />
        <SearchBar open = {open} Filtering = {FilterSearch}/>
        {isFiltered?filterReuslt:
        SideBarItems.map((item, index) => (
        <React.Fragment key={index}>{item}</React.Fragment>
        ))}
  </div>
        
  )
}

export default SideBarData
