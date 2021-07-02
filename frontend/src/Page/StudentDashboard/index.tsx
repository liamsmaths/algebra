import React from "react";
import { Table } from "antd";
import styled from "@emotion/styled";
import Text from "antd/lib/typography/Text";

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

const StudentDashboard = () => {
  const dataSource = [
    {
      key: "1",
      name: "Mike",
      age: 32,
      address: "10 Downing Street",
      questions: "5",
      totaltime: "15s",
    },
    {
      key: "2",
      name: "John",
      age: 42,
      address: "10 Downing Street",
      questions: "5",
      totaltime: "15s",
    },
    {
      key: "2",
      name: "John",
      age: 42,
      address: "10 Downing Street",
      questions: "5",
      totaltime: "15s",
    },
    {
      key: "2",
      name: "John",
      age: 42,
      address: "10 Downing Street",
      questions: "5",
      totaltime: "15s",
    },
    {
      key: "2",
      name: "John",
      age: 42,
      address: "10 Downing Street",
      questions: "5",
      totaltime: "15s",
    },
  ];

  const columns = [
    {
      title: "Algebra Topic",
      dataIndex: "name",
      key: "name",
    },
    {
      title: "Attempted",
      dataIndex: "age",
      key: "age",
    },
    {
      title: "Passed",
      dataIndex: "address",
      key: "address",
    },
    {
      title: "Question Attempted",
      dataIndex: "questions",
      key: "address",
    },
    {
      title: "Total time",
      dataIndex: "totaltime",
      key: "address",
    },
  ];

  return (
    <React.Fragment>
      <Details>
        <Text></Text>
      </Details>
      <StyledTable pagination={false} dataSource={dataSource} columns={columns} />
    </React.Fragment>
  );
};
export default StudentDashboard;
