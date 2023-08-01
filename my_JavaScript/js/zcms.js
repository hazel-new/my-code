import '../App.css'
import { PlusOutlined } from '@ant-design/icons';
import { Divider, Input, Select, Space, Button } from 'antd';
import React, { useState, useRef, useEffect } from 'react';
import cookie from "react-cookies";
import axios from 'axios';
import Selector from '../components/form/Selector';

// Virtual Router Partition page
// Demo:
//  ___________________________________________
// | Home                                      |
// |___________________________________________|
// 

const { TextArea } = Input;

const onSearch = (value) => {
  console.log('search:', value);
};

const Show = (props) => {
  const [items, setItems] = useState(['']);
  const [name, setName] = useState('');
  const [parentTicket, setParentTicket] = useState('');
  const [additionalInput, setAdditionalInput] = useState('');
  const [td_link, setTd_link] = useState('');
  const [ir_link, setIr_link] = useState('');
  const [tenant, setTenant] = useState('');
  const [technology, setTechnology] = useState('');
  const [descriptiveName, setDescriptiveName] = useState('');
  const [intendedUsers, setIntendedUsers] = useState('');
  const [usedFor, setUsedFor] = useState('');
  const [site, setSite] = useState('');
  const [type, setType] = useState('');
  const [optional, setOptional] = useState('');

  const userName = cookie.load("username")
  const loginName = userName == null ? "guest" : userName

  const inputRef = useRef(null);

  const handleSubmit = (event) => {
    console.log('you click submit button:', event.target.value);
    event.preventDefault();
    // -------------------------------------payload you need fulfill--------------------------------------------
    // let data = {
    //   "payload": {
    //     parent_cil: parentTicket,
    //     partition_name: vrName,
    //     reporter_signum: loginName,
    //     description: productInfo,
    //     additional_description: additionalInput,
    //     td_link: td_link,
    //     ir_link: ir_link
    //   }
    // }
    // ----------------------------------------------end--------------------------------------------------------

    // ----------------------------------------payload example--------------------------------------------------   
    let data = 
    {
      "payload":
               {
                "tenant":"npee","request_type":"standard","parent_ticket_id":"CIL-43033",
                "reporter_signum":"eiusdas","request_status": "new","desc_mandatory":"access",
                "desc_optional":"Please view this link[CIL-28]","selected_vr_name":"automation_test_sleep40_ts",
                "target_design_link":"test1","supporting_info":"motivation","security_profile": "trusted"
               }
    }
    // ----------------------------------------------end--------------------------------------------------------

    alert(JSON.stringify(data));
    //submit(data);   // post data
    //getApiTest();   // test Get api
    putApiTest();     // test Put api
  }

  const submit = (data) => {
    // check fastApi docs from backend first, if you get error with this url, you can check the url with backend team
    //const url = `http://100.78.133.197:5005/docs#/`;     // it is the api docs for frontend to test
    
    // db_post api from backend, if you get error with this url, you can check the url with backend team
    const url = `http://100.78.133.197:5005/db_post/`;     // test ok! with payload example

    console.log("you should check the api on fastApi docs first, now the url is: ", url);
    axios
        .post(url, data, {
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          }
        })
        .then((res) => {
            if (res.data) {
                console.log("post response:", res.data);
                alert('You are creating virtual router....');
                //window.location.reload(true);
            }
            else {
                alert('Please try again.');
            }
        })
        .catch(err => {
            //this.setCookie("loginError", err);
            Promise.reject(err);
        })
  }

  const getApiTest = () => {
    // fastApi docs from backend, if you get error with this url, you can check the url with backend team
    //const url = `http://100.78.133.197:5005/docs#/`;                    // it is the api docs for frontend to test
  
    // Get api from backend, if you get error with this url, you can check the url with backend team
    //const url = `http://100.78.133.197:5005/db_get/webpage_details`;    // test ok!
    //const url = `http://100.78.133.197:5005/db_get/vr_standard_desc`;   // test ok!
    //const url = `http://100.78.133.197:5005/history`;                   // test ok!
    const url = `http://100.78.133.197:5005/db_get/history/specific?webpage_id=https%3A%2F%2FVIR-67`;   //webpage_id string in query, you can check in VirtualRouter API UI first, e.g https%3A%2F%2FVIR-67.  test ok!
    //const url = `http://100.78.133.197:5005/db_get/VIR-143`;            //{webpage_id} string in path, e.g VIR-143.                 test ok!

    console.log("get url:", url);
    axios
        .get(url)
        .then((res) => {
            if (res.data) {
                console.log("get api response:", res.data);
                alert('You are testing the get api ...');
                //window.location.reload(true);
            }
            else {
                alert('Please try again.');
            }
        })
        .catch(err => {
            //this.setCookie("loginError", err);
            Promise.reject(err);
        })
    };

  const putApiTest = () => {

    // ----------------------------payload example----------------------------------
    let data = 
    {
      "payload": {"request_status": "new"}
    }
    // -------------------------------end-------------------------------------------

    // check fastApi docs from backend first, if you get error with this url, you can check the url with backend team
    //const url = `http://100.78.133.197:5005/docs#/`;                // it is the api docs for frontend to test

    const url = `http://100.78.133.197:5005/db_update/VIR-76`;       //{webpage_id} string in path,e.g VIR-143. 
    console.log("Put url:", url);

    axios
        .put(url, data, {
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          }
        })
        .then((res) => {
            if (res.data) {
                console.log("put response:", res.data);
                alert('You are update virtual router....');
                //window.location.reload(true);
            }
            else {
                alert('Please try again.');
            }
        })
        .catch(err => {
            //this.setCookie("loginError", err);
            Promise.reject(err);
        })
    };
  
  // functions handleTenantValue, to set tenant value in the dropdown item
  const handleTenantValue = (value, e) => {
    if (e === undefined) {
      setTenant('')
      return
    }
    setTenant(value)
  }

  // functions handleTechnologyValue, to set technology value in the dropdown item
  const handleTechnologyValue = (value, e) => {
    if (e === undefined) {
      setTechnology('')
      return
    }
    setTechnology(value)
  }

  // functions handleDescriptiveNameValue, to set descriptive name value in the dropdown item
  const handleDescriptiveNameValue = (value, e) => {
    if (e === undefined) {
      setDescriptiveName('')
      return
    }
    setDescriptiveName(value)
  }

  // functions handleIntendedUsersValue, to set intended users value in the dropdown item
  const handleIntendedUsersValue = (value, e) => {
    if (e === undefined) {
      setIntendedUsers('')
      return
    }
    setIntendedUsers(value)
  }

  // functions handleUsedForValue, to set used for value in the dropdown item
  const handleUsedForValue = (value, e) => {
    if (e === undefined) {
      setUsedFor('')
      return
    }
    setUsedFor(value)
  }

  // functions handleSiteValue, to set site value in the dropdown item
  const handleSiteValue = (value, e) => {
    if (e === undefined) {
      setSite('')
      return
    }
    setSite(value)
  }

  // functions handleTypeValue, to set type value in the dropdown item
  const handleTypeValue = (value, e) => {
    if (e === undefined) {
      setType('')
      return
    }
    setType(value)
  }

  // functions handleOptionalValue, to set optional value in the dropdown item
  const handleOptionalValue = (value, e) => {
    if (e === undefined) {
      setOptional('')
      return
    }
    setOptional(value)
  }


  // intendedUserForValue variable is used for collecting the (intended users) and (used for) dropdown item, please see https://eteamspace.internal.ericsson.com/display/LNP/Virtual+Router%3A+Standard+Descriptions
  let intendedUserForValue = ''

  // vrName variable is used for collecting the eight dropdown items 
  //include tenant/technology/descriptiveName/intendedUsers/usedFor/site/type/optional
  let vrName = ''

  // productInfo variable is the Standard Description,please see https://eteamspace.internal.ericsson.com/display/LNP/Virtual+Router%3A+Standard+Descriptions
  let productInfo = ''

  // these eight options as the selector's options parameter, not defined in front end, need get from backend with json file, TO DO.....
  const tenant_options = [
    {
        label: 'Approved Name',
        options: [
            {label: 'npee',value: 'npee',},
            {label: 'lpee',value: 'lpee',},
            {label: 'npeeDev',value: 'npeeDev',},
            {label: 'dnewStaging',value: 'dnewStaging',},
            {label: 'xnpee',value: 'xnpee',},
        ],
    },
    {
        label: 'Special cases',
        options: [
            {label: 'npoooee',value: 'npoooee',},
            {label: 'lpoooee',value: 'lpoooee',},
        ],
    },
  ]
  const technology_options = [
    {
        label: 'Approved Name',
        options: [
            {label: '6g5g4g3g2g',value: '6g5g4g3g2g',},
            {label: 'misc',value: 'misc',},
            {label: 'ee',value: 'ee',},
            {label: 'tp',value: 'tp',},
            {label: 'ops',value: 'ops',},
        ],
    },
  ]
  const descriptiveName_options = [
    {
        label: 'Approved Name',
        options: [
            {label: 'bbi',value: 'bbi',},
            {label: 'cds',value: 'cds',},
            {label: 'tp',value: 'tp',},
            {label: 'common-sero',value: 'common-sero',},
        ],
    },
    {
        label: 'Special cases',
        options: [
            {label: 'miscellaneous',value: 'miscellaneous',},
        ],
    },
  ]
  const intendedUsers_options = [
    {
        label: 'Approved Name',
        options: [
            {label: 'partner',value: 'partner',},
            {label: 'eri',value: 'eri',},
            {label: 'flera',value: 'flera',},
            {label: 'exempel',value: 'exempel',},
        ],
    },
  ]
  const usedFor_options = [
    {
        label: 'Approved Name',
        options: [
            {label: 'access',value: 'access',},
            {label: 'tools',value: 'tools',},
            {label: 'web',value: 'web',},
            {label: 'service',value: 'service',},
        ],
    },
    {
        label: 'RAN partitions',
        options: [
            {label: 'ran',value: 'ran',},
            {label: 'om-ran',value: 'om-ran',},
            {label: 'lmt',value: 'lmt',},
            {label: 'pran',value: 'pran',},
            {label: 'fronthaul',value: 'fronthaul',},
            {label: 'iac',value: 'iac',},
            {label: 'gte',value: 'gte',},
        ],
    },
    {
        label: 'Other TE partitions',
        options: [
            {label: 'oob',value: 'oob',},
            {label: 'mgmt',value: 'mgmt',},
        ],
    },
  ]
  const site_options = [
    {
        label: 'Approved Name',
        options: [
            {label: 'gp',value: 'gp',},
            {label: 'sero',value: 'sero',},
        ],
    },
  ]
  const type_options = [
    {
        label: 'Approved Name',
        options: [
            {label: 'trusted',value: 'trusted',},
            {label: 'untrusted',value: 'untrusted',},
            {label: 'secured',value: 'secured',},
        ],
    },
  ]
  const optional_options = [
    {
        label: 'Approved Name',
        options: [
            {label: 'caas',value: 'caas',},
            {label: 'daas',value: 'daas',},
            {label: 'caas-daas',value: 'caas-daas',},
            {label: 'legacy',value: 'legacy',},
            {label: 'internet',value: 'internet',},
            {label: 'RESTRICTED',value: 'RESTRICTED',},
            {label: 'NO-INTERNET',value: 'NO-INTERNET',},
        ],
    },
  ]
  //---------------------these eight options as the selector's options parameter END-----------------------------------------------------------------

  
  // intendedUserFor variable is used for match the intendedUserForValue and the Standard Description,please see https://eteamspace.internal.ericsson.com/display/LNP/Virtual+Router%3A+Standard+Descriptions
  // it need to improve because it wil get from backend, not defined in the frontend, TO DO.....
  const intendedUserFor = [
    { key: 'eri_access', value: 'Access partition for Ericsson users.' },
    { key: 'partner_access', value: 'Access partition for users from the specific partner.' },
    { key: 'eri_tools', value: 'Tools partition for development by Ericsson users.' },
    { key: 'partner_tools', value: 'Tools partition for development by Ericsson users & partners.' },
    { key: 'eri_web', value: 'Partition for WEB services that need to access a limited storage area / areas. For Ericsson users only.' },
    { key: 'partner_web', value: 'Partition for WEB services that need to access a limited storage area / areas. For Ericsson users & partners.' },
    { key: 'service', value: 'DNEW common services. Can be Global or Site specific partition.' },
    { key: 'mgmt', value: 'Tools partition for management interfaces console servers and other tools.' },
    { key: 'mgmt-gte', value: 'Tools partition for management interfaces of GTE (=GPRS Test Environment??).' },
    { key: 'mgmt-bmc', value: 'Tools partition for management interfaces for BMC.' },
    { key: 'mgmt-cloud', value: 'Management partiton for Cloud: VIM (openstack).' },
    { key: 'tools-automation', value: 'Tools partition for equipment used for NW and Zero Day STP automation.' },
    { key: 'fronthaul', value: 'Fronthaul partition network between RRU and DU.' },
    { key: 'iac', value: 'IAC - Simulated Internet (Traffic simulators).' },
    { key: 'pran', value: 'PRAN - RAN Control Plan (CP) and User Plane (UP).' },
    { key: 'om-ran', value: 'OM-RAN - RAN equipment management.' },
    { key: 'lmt', value: 'LMT - RAN Local Maintenance Terminal.' },
    { key: 'oob', value: 'Partitions for OOB equipment. (Out Of Band traffic).' },
    { key: 'mgmt-oob', value: 'OOB = Out Of Band. Management interface network.' }
  ]

  // selectedInfo is used for store all the dropdown item value
  const selectedInfo = [
    tenant,
    technology,
    descriptiveName,
    intendedUsers,
    usedFor,
    site,
    type,
    optional
  ]

  // userInputInfo variable is used for session store and set the some value
  const userInputInfo = [
    { name: 'parentTicket', value: parentTicket, handleEvent: setParentTicket },
    { name: 'tenant', value: tenant, handleEvent: setTenant },
    { name: 'technology', value: technology, handleEvent: setTechnology },
    { name: 'descriptiveName', value: descriptiveName, handleEvent: setDescriptiveName },
    { name: 'intendedUsers', value: intendedUsers, handleEvent: setIntendedUsers },
    { name: 'usedFor', value: usedFor, handleEvent: setUsedFor },
    { name: 'site', value: site, handleEvent: setSite },
    { name: 'type', value: type, handleEvent: setType },
    { name: 'optional', value: optional, handleEvent: setOptional },
    { name: 'vrName', value: vrName, handleEvent: null },
    { name: 'productInfo', value: productInfo, handleEvent: null },
    { name: 'additionalInput', value: additionalInput, handleEvent: setAdditionalInput },
    { name: 'td_link', value: td_link, handleEvent: setTd_link },
    { name: 'ir_link', value: ir_link, handleEvent: setIr_link }
  ]

  // intendedUserForInfo variable is used for storing intendedUsers and usedFor 
  const intendedUserForInfo = [intendedUsers, usedFor]

  // this function is used for splicing <intendedUsers> and <usedFor> together by _ 
  intendedUserForInfo.forEach((item, index) => {
    if (item && index < intendedUserForInfo.length - 1)
      item += '_'
    else if (item)
      item += ''
    intendedUserForValue += item
  })

  // this function is used for splicing all the required dropdown item together by _
  selectedInfo.forEach((item, index) => {
    console.log("item : ", item)
    if (item && index < selectedInfo.length - 1) {
      item += '_'
    } 
    // if Optinal dropdown item is not empty,splicing all the dropdown item together by _ 
    //eg. selectedInfo = <tenant>_<technology>_<descriptiveName>_<intendedUsers>_<usedFor>_<site>_<type>  if Optional dropdown is empty.
    if (item === '' && index === selectedInfo.length - 1 && type) {
      vrName = (vrName.charAt(vrName.length - 1) === '_') ? vrName.slice(0, vrName.length - 1) : vrName
    }
    vrName += item
  })

  // intendedUserForValue variable is used for describe the partition type, please see https://eteamspace.internal.ericsson.com/display/LNP/Virtual+Router%3A+Standard+Descriptions
  // if intendedUserForValue doesn't match the https://eteamspace.internal.ericsson.com/display/LNP/Virtual+Router%3A+Standard+Descriptions, productInfo will be 'No special description.' 
  intendedUserFor.forEach((item) => {
    if (item.key === intendedUserForValue) {
      productInfo = item.value
    }
    else if(intendedUserForValue !== '' && item.key !== intendedUserForValue){
      productInfo = 'No special description.'
    }
  })
  // if the productInfo is null, usually when user first open the VR page, all the dropdown item is empty, so it need to wait for user to select.
  productInfo = productInfo ? productInfo : 'Waiting for user to select the VR name above.'

  // Save function 
  const handleSaveDate = (event, e) => {
    if (e === undefined) {
      console.log('e = undefined:', e);
      //setOptional('')
      //return
    }
    console.log("save date", event.value, "e: ", e)
    userInputInfo.forEach(item => (
      console.log("item:", item, "item.name:", item.name, typeof(item.name), "item.value:", item.value,typeof(item.value)),
      sessionStorage.setItem(item.name, item.value)))
  }

  // clear function
  const handleClearDate = (event, e) => {
    console.log('ClearDate:', event.target.value);
    //event.preventDefault();
    if (e === undefined) {
      console.log('e = undefined:', e);
      //setOptional('')
      //return
    }
    console.log("clear date：", event.value, " e: ", e)
    sessionStorage.clear();
    setParentTicket('')
    setTenant('')
    setTechnology('')
    setIntendedUsers('')
    setUsedFor('')
    setSite('')
    setType('')
    setOptional('')
    setDescriptiveName('')
    setAdditionalInput('')
    setTd_link('')
    setIr_link('')
  }

  useEffect(() => {
    userInputInfo.forEach(item => {
      if (item.name !== 'vrName' && item.name !== 'productInfo') {
        item.value = sessionStorage.getItem(item.name)
        if ((item.value !== '' || item.handleEvent !== null) && item.value !== null) {
          item.handleEvent(item.value)
        }
      }
    })  
  },[]
  )

  return (
    <React.Fragment>
      <table for="parentTicket" cellPadding={10} cellSpacing={5}>&nbsp;&nbsp;Parent ticket:
        <input
          id="parentTicket"
          name="parentTicket"
          type="text"
          onChange={(e) => setParentTicket(e.target.value)}
          value={parentTicket}
        />
      </table>
      <br />
      <text>&nbsp;&nbsp;All the bellow fields are mandatory, except the last field that is Optional.
        Depending on the use case, the Optional field must be filled.</text>
      <table cellPadding={10} cellSpacing={5}>
        <thead>
          <tr>
            <th >tenant</th>
            <th >technology</th>
            <th >descriptive name</th>
            <th >intended user</th>
            <th >used for</th>
            <th >site</th>
            <th >type</th>
            <th>Optional</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td ><label></label>
              <Selector
                defaultValue={sessionStorage.getItem('tenant') ? sessionStorage.getItem('tenant') : "---select---"}
                onChange={handleTenantValue}
                value={tenant}
                onSearch={onSearch}
                options={tenant_options}>
              </Selector>
            </td>
            <td><label></label>
              <Selector
                defaultValue={sessionStorage.getItem('technology') ? sessionStorage.getItem('technology') : "---select---"}
                onChange={handleTechnologyValue}
                value={technology}
                onSearch={onSearch}
                options={technology_options}>
              </Selector>
            </td>
            <td><label></label>
              <Selector
                defaultValue={sessionStorage.getItem('descriptiveName') ? sessionStorage.getItem('descriptiveName') : "---select---"}
                onChange={handleDescriptiveNameValue}
                value={descriptiveName}
                onSearch={onSearch}
                options={descriptiveName_options}>
              </Selector>
            </td>
            <td><label></label>
              <Selector
                defaultValue={sessionStorage.getItem('intendedUsers') ? sessionStorage.getItem('intendedUsers') : "---select---"}
                onChange={handleIntendedUsersValue}
                value={intendedUsers}
                onSearch={onSearch}
                options={intendedUsers_options}>
              </Selector>
            </td>
            <td><label></label>
              <Selector
                defaultValue={sessionStorage.getItem('usedFor') ? sessionStorage.getItem('usedFor') : "---select---"}
                onChange={handleUsedForValue}
                value={usedFor}
                onSearch={onSearch}
                options={usedFor_options}>
              </Selector>
            </td>
            <td><label></label>
              <Selector
                defaultValue={sessionStorage.getItem('site') ? sessionStorage.getItem('site') : "---select---"}
                onChange={handleSiteValue}
                value={site}
                onSearch={onSearch}
                options={site_options}>
              </Selector>
            </td>
            <td><label></label>
              <Selector
                defaultValue={sessionStorage.getItem('type') ? sessionStorage.getItem('type') : "---select---"}
                onChange={handleTypeValue}
                value={type}
                onSearch={onSearch}
                options={type_options}>
              </Selector>
            </td>
            <td><label></label>
              <Selector
                defaultValue={sessionStorage.getItem('optional') ? sessionStorage.getItem('optional') : "---select---"}
                onChange={handleOptionalValue}
                value={optional}
                onSearch={onSearch}
                options={optional_options}>
              </Selector>
            </td>
          </tr>
        </tbody>
      </table>
      <br />
      <table for="productionDescription">&nbsp;&nbsp;Virtual Router name (Partition) according to above selection:
        <br />
        <Input
          style={{
            width: 400,
            resize: 'none',
          }}
          value={vrName}
        />
        <br />
      </table>
      <br />

      <br />
      <br />
      <br />
      <br />

      <table for="productionDescription">&nbsp;&nbsp;Description. Predefined according to selected VR name.
        <br />
        &nbsp;&nbsp;The automation define this part of the description:
        <br />
        <TextArea
          style={{
            height: 80,
            width: 500,
            resize: 'none',
          }}
          value={productInfo}
        />
        <br />
      </table>
      <br />
      <table for="additionalDescription">&nbsp;&nbsp;Description. Additional input from user, that will be added to the predefined description. (Optional)
        <br />
        &nbsp;&nbsp;If added, keep it short, like "LSF cluster".
        <br />
        <TextArea
          //showCount
          maxLength={250}
          style={{
            height: 120,
            width: 500,
          }}
          onChange={(e) => setAdditionalInput(e.target.value)}
          value={additionalInput}
        />
        <span className="remainWords">{additionalInput.length}/250</span>

        <br />
      </table>
      <br />
      <table for="supportInformation">&nbsp;&nbsp;Target Design, or Service Design link. Other supporting information link is allowed.
        <br />
        &nbsp;&nbsp;Mandatory or Optional, depending on Tenant. See system feedback, It depends on the Tenant of choice.
        <br />
        <TextArea
          style={{
            height: 100,
            width: 500,
            resize: 'none',
          }}
          onChange={(e) => setTd_link(e.target.value)}
          value={td_link}
        />
        <br />
      </table>
      <br />
      <table for="ir_link">&nbsp;&nbsp;Target Design, Approved link:
        <br />
        <TextArea
          style={{
            height: 50,
            width: 500,
            resize: 'none',
          }}
          onChange={(e) => setIr_link(e.target.value)}
          value={ir_link}
        />
        <br />
      </table>
      <br />
      <div>
        <button type="Submit" value="Save" style={{ float: "left", marginRight: "40px", width: 80 }} onClick={handleSaveDate}>Save</button>
        <button type="Submit" value="Clear" style={{ float: "left", marginLeft: "0px", width: 80 }} onClick={handleClearDate}>Clear</button>
        {/* user must select or text <tenant> <technology> <descriptiveName> <intendedUsers> <usedFor> <site> <type> <td_link> <ir_link> before submit, because those item is required  */}
        <button type="Submit" value="Submit" style={{ float: "left", marginLeft: "40px", width: 80 }} onClick={handleSubmit}
          disabled={
            tenant.length < 1 ||
            technology.length < 1 ||
            descriptiveName.length < 1 ||
            intendedUsers.length < 1 ||
            usedFor.length < 1 ||
            site.length < 1 ||
            type.length < 1 ||
            td_link.length < 1 ||
            ir_link.length < 1
          }
          autocomplete="off"
        >Submit</button>
      </div>
    </React.Fragment>
  );
};
export default Show;
