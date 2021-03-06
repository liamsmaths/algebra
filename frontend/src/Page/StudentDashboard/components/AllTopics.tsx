import React, { useEffect, useState } from "react";
import { Table, Button, Progress } from "antd";
import styled from "@emotion/styled";
import Text from "antd/lib/typography/Text";
import axios from "axios";
import { useHistory } from "react-router-dom";
import { CloseOutlined, CheckOutlined } from "@ant-design/icons";
import jwt from "jwt-decode";

const StyledTable = styled(Table)`
  .ant-table table {
    background-color: #f4f8f9;
  }
  table {
    border-spacing: 0 10px !important;
  }
  .ant-table-thead > tr > th {
    border: none;
    background: none;
    padding: 0px 16px;
    font-size: 18px;
  }
  .ant-table-tbody > tr > td {
    border: none;
    padding: 12px 16px;
  }

  .ant-table-row {
    border-radius: 10px !important;
    box-shadow: 1px 1px 10px #1c3faa1a !important;
    background-color: white;
    textAlign: 'center';
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
  const token: any = localStorage.getItem("token");
  const user: any = jwt(token);

  var currentStudentTopics: any = [];

  const handleTryOut = (item: any) => {
    history.push({
      pathname: "/practiceboard",
      state: {
        id: item.id,
        name: item.name,
        studentTopicId: item.student_topic_id,
      },
    });
  };

  const columns = [
    {
      title: "Algebra Topic",
      dataIndex: "name",
      key: "name",
      render: (name: any, record: any) => (
        <div onClick={() => handleTryOut(record)} style={{ cursor: "pointer" }}>
          {name}
        </div>
      ),
    },
    {
      title: "Passed",
      dataIndex: "has_passed",
      key: "has_passed",
      render: (has_passed: any) => (
        <React.Fragment>
          {has_passed === null ? null : has_passed === true ? (
            <CheckOutlined style={{ color: "green" }} />
          ) : (
            <CloseOutlined style={{ color: "red" }} />
          )}
        </React.Fragment>
      ),
    },
    {
      title: "Questions Attempted",
      dataIndex: "total_attempts",
      key: "total_attempts",
    },
    {
      title: "Last Attempt",
      dataIndex: "last_attempt",
      key: "last_attempt",
      render: (item: any) => (
        <React.Fragment>{item === null ? "" : new Date(item).toLocaleDateString()}</React.Fragment>
      ),
    },
    {
      title: "Progress",
      dataIndex: "id",
      key: "id",
      render: (id: any, record: any) => {
        if (record.correct_answer != null) {
          if(record.correct_answer < 5){ 
          const correctAttemptPercentage = Math.round(
            (record.correct_answer / 5) * 100
          );
          return <Progress percent={correctAttemptPercentage} size="small" />;
        }
          else{
            const correctAttemptPercentage = 100;
            return <Progress percent={correctAttemptPercentage} size="small" />;
          }
          
        }
      
      },
    },
  ];

  const fetchAllTopics = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/getAllTopics");
      setAllTopics(response.data);
    } catch (e) {}
  };

  useEffect(() => {
    fetchAllTopics();
  }, []);

  const getCurrentStudentTopic = (item: any) => {
    const currentId = item.id;
    const currentName = item.name;
    const currentStudent = item.student_topics.filter(
      (item: any) => item.student_id === user.id
    );
    const currentHasPassed = currentStudent.length > 0 ? currentStudent[0].has_passed : null;
    const currentTotalAttempts =
      currentStudent.length > 0 ? currentStudent[0].total_attempts : null;
    const currentLastAttempt = currentStudent.length > 0 ? currentStudent[0].last_attempt : null;
    const currentStudentTopicId =
      currentStudent.length > 0 ? currentStudent[0].student_topic_id : null;
    const currentAnswer = currentStudent.length > 0 ? currentStudent[0].correct_answer : null;
    const newArray: any = {
      id: currentId,
      name: currentName,
      has_passed: currentHasPassed,
      total_attempts: currentTotalAttempts,
      last_attempt: currentLastAttempt,
      student_topic_id: currentStudentTopicId,
      correct_answer: currentAnswer,
    };

    currentStudentTopics.push(newArray);
  };

  allTopics &&
    allTopics.map((item: any) => {
      getCurrentStudentTopic(item);
    });

  return (
    <React.Fragment>
      <StyledTable pagination={false} dataSource={currentStudentTopics} columns={columns} />
    </React.Fragment>
  );
};
export default AllTopics;
