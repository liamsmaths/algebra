import React from "react";
import styled from "@emotion/styled";
import Text from "antd/lib/typography/Text";
import { createFromIconfontCN } from "@ant-design/icons";
import { Popover } from "antd";

const IconFont = createFromIconfontCN({
  scriptUrl: "//at.alicdn.com/t/font_2643792_vtsize76u7.js",
});

const Wrapper = styled("div")`
  padding: 27px 12px 0px 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
`;
const DetailsWrapper = styled("div")`
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 130px;
`;

const HeaderComponent = () => {
  return (
    <Wrapper>
      <Text
        style={{ fontSize: "26px", color: "white", textTransform: "uppercase", letterSpacing: 2 }}
      >
        Algebra Topic
      </Text>
      <DetailsWrapper>
        <Text style={{ fontSize: "20px", color: "white" }}>John Smith</Text>
        <Popover placement="bottom" title="" content={<Text>Logout</Text>} trigger="click">
          <IconFont type="icon-setting" style={{ fontSize: "20px", color: "white" }} />
        </Popover>
      </DetailsWrapper>
    </Wrapper>
  );
};
export default HeaderComponent;
