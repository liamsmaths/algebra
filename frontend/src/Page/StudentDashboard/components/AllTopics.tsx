import React, { useEffect, useState } from "react";
import { Table, Button, Divider } from "antd";
import styled from "@emotion/styled";
import Text from "antd/lib/typography/Text";
import axios from "axios";
import { useHistory } from "react-router-dom";
import MyTopics from "./MyTopics";

const StyledTable = styled(Table)`
  table {
    border-spacing: 0 10px !important;
  }
  .ant-table-thead > tr > th {
    border: none;
    background: none;
    padding: 0px 16px;
  }
  .ant-table-tbody > tr > td {
    border: none;
    padding: 12px 16px;
  }

  .ant-table-row {
    border-radius: 10px !important;
    box-shadow: 1px 1px 10px #1c3faa1a !important;
  }

  .ant-pagination-item,
  .ant-pagination-item-link {
    border-radius: 50% !important;
  }
  .ant-pagination-item-active {
    border: none;
    background: #2680eb;
    a {
      color: white !important;
    }
  }
`;

const Details = styled("div")`
  padding: 10px 0px 20px 0px;
`;
const StyledButton = styled(Button)`
  background: #6d60b0;
  color: white;
  border-radius: 5px;
  height: 35px;
  &:hover,
  &:focus {
    background: #6d60b0;
    color: white;
  }
  border: none;
`;

const AllTopics = () => {
  const [allTopics, setAllTopics] = useState<any>();
  const history = useHistory();

  const handleTryOut = (item: any) => {
    history.push({
      pathname: "/practiceboard",
      state: { id: item.id, name: item.name },
    });
  };

  const columns = [
    {
      title: "Algebra Topic",
      dataIndex: "name",
      key: "name",
    },

    {
      title: "Action",
      dataIndex: "id",
      key: "id",
      render: (id: any, record: any) => (
        <React.Fragment>
          <StyledButton onClick={() => handleTryOut(record)}>Try it out</StyledButton>
        </React.Fragment>
      ),
    },
  ];

  const fetchAllTopics = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/getAllTopics");
      setAllTopics(response);
    } catch (e) {}
  };

  useEffect(() => {
    fetchAllTopics();
  }, []);

  return (
    <React.Fragment>
      <Details>
        <Divider orientation="left">All Topics</Divider>
      </Details>
      <StyledTable pagination={false} dataSource={allTopics && allTopics.data} columns={columns} />
      <MyTopics />
    </React.Fragment>
  );
};
export default AllTopics;
