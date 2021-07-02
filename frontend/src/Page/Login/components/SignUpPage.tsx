import React, { useState, useEffect } from "react";
import {
  Col,
  Row,
  Form,
  Input,
  Typography,
  Checkbox,
  notification,
  Modal,
  Select,
  Button,
} from "antd";
import styled from "@emotion/styled";
// import ActionButton from "../../../components/ActionButton";

import { EyeOutlined, EyeInvisibleOutlined } from "@ant-design/icons";
import Verification from "../../../image/login.jpg";

const { Title, Text } = Typography;
const { Option } = Select;

const StyledLogoContainer = styled(Row)`
  margin-bottom: 1.5em;
`;
const StyledLogo = styled("img")`
  max-width: 100%;
  width: 50%;
  object-fit: contain;
  height: auto;
`;
const StyledLoginForm = styled(Col)`
  box-shadow: -3px 18px 35px rgba(0, 0, 0, 0.12);
  padding: 2em 5em 1px 4.5em;
  @media only screen and (max-width: 1024px) {
    padding: 40px 40px 20px 40px;
  }
  background: #f2fbff;
  min-height: 85vh;
`;
const StyledInput = styled(Input)`
  border-radius: 5px;
  // margin-top: 30px;
  :active,
  :focus {
    border-color: #1dce78;
    outline: none;
  }
`;
const StyledContact = styled(Input)`
  border-radius: 5px;
  width: 100% !important;
  :active,
  :focus {
    border-color: #1dce78;
    outline: none;
  }
`;

const StyledForm = styled(Form)`
  height: 100%;
  padding-bottom: 10px;
  .ant-form-item {
    margin-bottom: 0px;
  }
  .ant-form-item-label {
    padding: 0;
    font-size: 0.8em;
  }
`;
const StyledCheckbox = styled(Checkbox)`
  margin: 1em 0 0;

  .ant-checkbox-inner {
    border-color: #1dce78;
  }
  .ant-checkbox-checked {
    .ant-checkbox-inner {
      border-color: #1dce78;
      background-color: #1dce78;
    }
  }
`;
const StyledLink = styled("a")`
  color: #18ca74 !important;
  font-weight: 500;
`;

const StyledIconSwitch = styled("span")`
  cursor: pointer;
  position: absolute;
  right: 15px;
  top: 5px;
  font-size: 18px;
  z-index: 1;
`;
const StyledModal = styled(Modal)`
  .ant-modal-content {
    background: #c9fde3;
    position: relative;
    overflow: hidden;
    &::before {
      content: "";
      width: 200px;
      height: 200px;
      background: rgba(255, 255, 255, 0.3);
      border-radius: 50%;
      position: absolute;
      top: -130px;
      right: 60px;
    }
    &::after {
      content: "";
      width: 300px;
      height: 300px;
      background: rgba(255, 255, 255, 0.3);
      border-radius: 50%;
      position: absolute;
      top: -170px;
      right: -140px;
    }
  }
  .ant-modal-header,
  .ant-modal-body {
    background: transparent;
  }
  .ant-modal-footer {
    display: none !important;
  }
`;
const StyledDiv = styled.div`
  text-align: center;
  margin: 30px 0 30px 0;
`;
const StyledLabel = styled.span`
  font-size: 16px;
  font-weight: 500;
  text-align: center;
`;
const ImageWrapper = styled.div`
  width: 80px;
  height: 80px;
  border-radius: 50%;
  text-align: center;
  margin-bottom: 15px;
  background: #baead4;
`;
const StyledImage = styled.img`
  height: 60px;
  width: 60px;
  margin-top: 10px;
`;
const StyledNumber = styled.span`
  font-weight: 500;
  font-size: 16px;
  letter-spacing: 1px;
  color: #18ca74;
`;

type SignUpFormProps = {
  setAnimation: any;
  animation: boolean;
};

const SignUpForm: React.SFC<SignUpFormProps> = ({ setAnimation, animation }) => {
  const [form] = Form.useForm();
  const [passwordVisible, setPasswordVisible] = useState(false);
  const [modalVisible, setModalVisible] = useState(false);
  const [isWithNumber, setIsWithNumber] = useState(false);
  const [enteredNumber, setEnteredNumber] = useState("");
  const [selectedCountry, setSelectedCountry] = useState("+1");

  const lastTwoNums = enteredNumber.substring(enteredNumber.length - 2);
  const closeModal = () => {
    setModalVisible(false);
  };
  const layout = {
    labelCol: {
      span: 8,
    },
    wrapperCol: {
      offset: 5,
      span: 14,
    },
  };

  //   const [{ data, loading }, makeRequest] = useAxios({
  //     method: "POST",
  //     url: "api/Account/GenerateCode",
  //   });

  //   useEffect(() => {
  //     makeRequest({});
  //   }, []);

  //   const handleResendRequest = () => {
  //     notification.open({
  //       message: "Success",
  //       description: "Verification code has been sent to your number!",
  //     });
  //     makeRequest({data: {
  //       PhoneNumber: enteredNumber.substring(enteredNumber.length-10),
  //       CountryCode: selectedCountry,
  //     }});
  //   }
  const handleCountry = (value: any) => {
    setSelectedCountry(value);
  };
  const handleModalVisible = () => {
    setModalVisible(true);
    setIsWithNumber(true);
  };

  const countrySelector = (
    <Form.Item name="country" noStyle>
      <Select defaultValue="+977" onChange={handleCountry}>
        <Option value="+1">US +1</Option>
        <Option value="+91">IN +91</Option>
        <Option value="+92">PK +92</Option>
        <Option value="+232">SL +232</Option>
        <Option value="+977">NP +977</Option>
      </Select>
    </Form.Item>
  );

  return (
    <StyledLoginForm>
      <StyledLogoContainer>
        {/* <Col>
          <StyledLogo src="http://alphaventus.com/wp-content/uploads/2018/12/PNG-2-e1545259945185.png" />
        </Col> */}
      </StyledLogoContainer>
      <Title style={{ fontSize: "1.5em" }}>Sign Up</Title>
      <Text type="secondary" style={{ fontSize: "15px", marginBottom: "1em", display: "block" }}>
        Create your free account and Get started.
      </Text>
      <StyledForm form={form} layout="vertical" size="large" hideRequiredMark>
        <Row gutter={24} style={{ marginBottom: "0" }}>
          <Col span={12}>
            <Form.Item
              label="First Name"
              name="firstName"
              rules={[
                { required: true, message: "Please enter First Name!" },
                {
                  pattern: /^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$/,
                  message: "Please Enter valid name",
                },
              ]}
            >
              <StyledInput style={{ textTransform: "capitalize" }} placeholder="Jack" />
            </Form.Item>
          </Col>
          <Col span={12}>
            <Form.Item
              label="Last Name"
              name="lastName"
              rules={[
                { required: true, message: "Please Enter Last Name!" },
                {
                  pattern: /^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$/,
                  message: "Please Enter valid name",
                },
              ]}
            >
              <StyledInput style={{ textTransform: "capitalize" }} placeholder="Smith" />
            </Form.Item>
          </Col>
        </Row>
        <Row gutter={24} style={{ marginBottom: "0" }}>
          <Col span={12}>
            <Form.Item
              label="E-mail"
              name="email"
              rules={[
                { required: true, message: "Please enter Email" },
                {
                  pattern: /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/,
                  message: "Please Enter valid Email",
                },
              ]}
            >
              <StyledInput placeholder="name@gmail" />
            </Form.Item>
          </Col>
          <Col span={12}>
            <Form.Item
              label="Phone Number"
              name="phoneNumber"
              rules={[
                { required: true, message: "Please Enter Phone Number" },
                {
                  pattern: /^\d{10}$/,
                  message: "Phone number is 10 digit number",
                },
              ]}
            >
              <StyledContact addonBefore={countrySelector} placeholder="1234567890" />
            </Form.Item>
          </Col>
        </Row>

        <Row gutter={24} style={{ marginBottom: "0" }}>
          <Col span={12}>
            <Form.Item
              label="Password"
              name="password"
              rules={[
                { required: true, message: "Please enter Password" },
                {
                  pattern: /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{6,}$/,
                  message: "Please enter valid password!",
                },
              ]}
            >
              <StyledInput type="password" />
            </Form.Item>
          </Col>
          <Col span={12}>
            <StyledIconSwitch onClick={() => setPasswordVisible(!passwordVisible)}>
              {passwordVisible ? <EyeOutlined /> : <EyeInvisibleOutlined />}
            </StyledIconSwitch>
            <Form.Item
              label="Confirm"
              name="confirm-password"
              rules={[
                { required: true, message: "Please confirm password" },
                ({ getFieldValue }) => ({
                  validator(rule, value) {
                    if (!value || getFieldValue("password") === value) {
                      return Promise.resolve();
                    }
                    return Promise.reject("Passwords do not match!");
                  },
                }),
              ]}
            >
              <StyledInput type={passwordVisible ? "text" : "password"} />
            </Form.Item>
          </Col>
        </Row>
        <Row>
          <Text style={{ fontSize: "0.7em", marginTop: "10px" }}>
            Use 6 or more characters with mix of atleast a capital letter,numbers and symbols
          </Text>
        </Row>
        <Form.Item
          name="agreement"
          valuePropName="checked"
          rules={[
            {
              validator: (_, value) =>
                value
                  ? Promise.resolve()
                  : Promise.reject(
                      <span style={{ fontSize: "12px" }}>
                        Please indicate that you have read and agree to the Terms and Conditions and
                        Privacy Policy
                      </span>
                    ),
            },
          ]}
        >
          <StyledCheckbox style={{ fontSize: "0.5em" }}>
            Registering to this website you accept our Terms of Use and our Privacy Policy
          </StyledCheckbox>
        </Form.Item>
        {/* <ActionButton
        size="large"
        style={{
          width: "100%",
          background: "#2AB471",
          borderRadius: "8px",
          fontSize: "1em",
        }}
        url="api/account/signup"
        onSuccess={(response: any) => {
          notification.open({
            message: "Success",
            description: "A verification code has been sent to your number!",
          });
          makeRequest({data: {
            PhoneNumber: enteredNumber.substring(enteredNumber.length-10),
            CountryCode: selectedCountry,
           }});
          setModalVisible(true);
        }}
        onError={(err: any) => {
          notification.open({
            message: "Error",
            description: err.message,
          });
        }}
        onSubmit={({ setFormData, setIsReady }: any) => {
          form
            .validateFields()
            .then((values) => {
              const { email, password,firstName,lastName,phoneNumber } = values;
              setFormData({
                FirstName: firstName,
                Email: email,
                LastName: lastName,
                Password: password,
                CountryCode: selectedCountry,
                PhoneNumber: phoneNumber.substring(phoneNumber.length-10),
                PhoneNumberTypeId: 1,
              });
              setEnteredNumber(phoneNumber);
              setIsReady(true);
            })
            .catch((errorInfo) => {
              console.log(errorInfo);
              setIsReady(false);
            });
        }}
      >
       Sign Up
      </ActionButton> */}
        <Button type="primary">Sign Up</Button>
      </StyledForm>
      <Row justify="center" align="middle" style={{ flexDirection: "column", margin: "1em 0" }}>
        <Col>
          <Text style={{ fontSize: "1em" }}>Already Registered and verified? </Text>
          <StyledLink onClick={() => setAnimation(!animation)}>Log In</StyledLink>
        </Col>
      </Row>
      {/* <Row
        justify="center"
        align="middle"
        style={{ flexDirection: "column", margin: "1em 0" }}
      >
        <Col>
          <Text style={{ fontSize: "1em" }}>Didn't recieve your verification code? </Text>
          <StyledLink onClick={handleModalVisible}>
            Resend Code
          </StyledLink>
        </Col>
      </Row> */}

      <StyledModal
        width="25%"
        title="Account Verification"
        visible={modalVisible}
        closable={true}
        onCancel={closeModal}
        destroyOnClose={true}
        maskClosable={false}
      >
        <Row justify="center">
          <ImageWrapper>
            <StyledImage src={Verification} />
          </ImageWrapper>
        </Row>
        <Row justify="center">
          <h2>One more step...</h2>
          {isWithNumber === true ? (
            <StyledLabel>Enter your number and your verification code</StyledLabel>
          ) : (
            <>
              <StyledLabel>
                A verification code has been sent to <br />
                <StyledNumber>
                  {" "}
                  XXX-XXX-XX{lastTwoNums.length > 0 ? lastTwoNums : "XX"}
                </StyledNumber>
                . Please enter
                <br /> the code to continue.
              </StyledLabel>
            </>
          )}
        </Row>
        <Form form={form} {...layout} name="verification" hideRequiredMark layout="vertical">
          {/* {
              isWithNumber &&
              <Form.Item
              label=""
              name="phoneNumber"
              rules={[
                {
                  required: true,
                  message: 'Please Enter Phone Number',
                },
              ]}
            >
              <StyledInput placeholder='9876543210' size="large" />
            </Form.Item>
            } */}

          <Form.Item
            label=""
            name="verificationCode"
            rules={[
              {
                required: true,
                message: "Please Enter Verification Code",
              },
            ]}
          >
            <StyledInput placeholder="Your code..." size="large" />
          </Form.Item>
        </Form>
        <StyledDiv>
          {/* <ActionButton
              method={"Post"}
              url={"api/Account/CheckCode"}
              size="large"
              style={{
                marginRight: "10px",
                borderRadius: "7px",
                background: "#18ca74",
                borderColor: "#fff",
              }}
              onSuccess={(response: any) => {
                console.log(response);
                notification.open({
                  message: "Success",
                  description: "Your account is created and verified!",
                });
                setModalVisible(false);
                // setIsWithNumber(false);
                setAnimation(!animation);
              }}
              onError={(err: any) => {
                notification.open({
                  message: "Error",
                  description: err.message,
                });
              }}
              onSubmit={({ setFormData, setIsReady }: any) => {
                form
                  .validateFields()
                  .then((values) => {
                    const {
                      verificationCode,
                    } = values;
                    setFormData({
                      PhoneNumber: enteredNumber.substring(enteredNumber.length-10),
                      CountryCode: selectedCountry,
                      Code: verificationCode,
                    });
                    setIsReady(true);
                  })
                  .catch((errorInfo) => {
                    console.log(errorInfo);
                    setIsReady(false);
                  });
              }}
            >
              Verify Account
            </ActionButton> */}
        </StyledDiv>
        <Row justify="center" align="middle" style={{ flexDirection: "column", margin: "1em 0" }}>
          <Col>
            <Text style={{ fontSize: "1em", fontWeight: 500 }}>
              Didn't recieve your verification code?{" "}
            </Text>
            {/* <StyledLink onClick={handleResendRequest}>
                Resend Code
              </StyledLink> */}
          </Col>
        </Row>
      </StyledModal>
    </StyledLoginForm>
  );
};

export default SignUpForm;
